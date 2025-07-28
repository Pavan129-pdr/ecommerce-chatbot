import React, { useState } from "react";
import axios from "axios";

function Chatbot() {
  const [input, setInput] = useState("");
  const [chat, setChat] = useState([]);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    setChat([...chat, userMessage]);

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", {
        message: input,
      });

      const botMessage = { sender: "bot", text: res.data.status || res.data.response || "No reply" };
      setChat(prev => [...prev, botMessage]);
    } catch (err) {
      setChat(prev => [...prev, { sender: "bot", text: "Error contacting server" }]);
    }

    setInput("");
  };

  return (
    <div style={{ padding: 20, maxWidth: 600, margin: "auto" }}>
      <h2>E-commerce Chatbot</h2>
      <div style={{ border: "1px solid #ccc", padding: 10, height: 300, overflowY: "scroll", marginBottom: 10 }}>
        {chat.map((msg, idx) => (
          <div key={idx} style={{ textAlign: msg.sender === "user" ? "right" : "left" }}>
            <b>{msg.sender === "user" ? "You" : "Bot"}:</b> {msg.text}
          </div>
        ))}
      </div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSend()}
        style={{ width: "80%", padding: 8 }}
        placeholder="Ask about your order, products..."
      />
      <button onClick={handleSend} style={{ padding: 8, marginLeft: 5 }}>Send</button>
    </div>
  );
}

export default Chatbot;
