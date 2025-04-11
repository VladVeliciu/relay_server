const express = require("express");
const axios = require("axios");
const app = express();

app.use(express.json());

const TARGET_URL = "https://tb-ai-server.onrender.com";

app.post("/", async (req, res) => {
  try {
    const data = req.body;

    // Log received data from ESP
    console.log("Received from ESP:", data);

    // Forward to your Render AI server
    const response = await axios.post(TARGET_URL, {
      features: data.features
    }, {
      headers: {
        "Content-Type": "application/json"
      }
    });

    // Relay response back to ESP
    res.json(response.data);
  } catch (error) {
    console.error("Forwarding failed:", error.message);
    res.status(500).json({ error: "Relay failed" });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Relay server listening on port ${PORT}`);
});
