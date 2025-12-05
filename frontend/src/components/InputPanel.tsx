// src/components/InputPanel.tsx
import React, { useState } from "react";
import { analyzeRemote } from "../lib/api";

type Props = {
  onResult: (data: any | null) => void;
};

export default function InputPanel({ onResult }: Props) {
  const [text, setText] = useState<string>("");
  const [sleep, setSleep] = useState<number>(7);
  const [loading, setLoading] = useState<boolean>(false);

  async function handleAnalyze() {
    if (!text.trim()) {
      alert("Please write something to analyze.");
      return;
    }

    setLoading(true);
    try {
      const payload = { user_id: "demo", text, sleep_hours: sleep };
      console.log("📤 InputPanel -> sending payload:", payload);

      const res = await analyzeRemote(payload);
      console.log("📥 InputPanel -> got response:", res);

      onResult(res);
    } catch (err) {
      console.error("Analyze failed:", err);
      alert("Analyze failed — check console for details.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="p-6 bg-white rounded-xl shadow-md">
      <label className="block mb-2 text-sm font-medium text-gray-700">How are you feeling today?</label>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Write how you feel..."
        className="w-full min-h-[100px] p-3 border rounded mb-4"
      />

      <div className="mb-4">
        <label className="text-sm text-gray-600">Hours of sleep last night: <strong>{sleep}h</strong></label>
        <input
          type="range"
          min={0}
          max={12}
          value={sleep}
          onChange={(e) => setSleep(Number(e.target.value))}
          className="w-full mt-2"
        />
      </div>

      <div className="flex gap-3">
        <button
          onClick={handleAnalyze}
          disabled={loading}
          className="px-6 py-3 rounded-lg bg-gradient-to-r from-blue-400 to-green-300 text-white shadow"
        >
          {loading ? "Analyzing..." : "Analyze Mood"}
        </button>
        <button
          onClick={() => { setText(""); setSleep(7); onResult(null); }}
          className="px-4 py-3 border rounded-lg"
        >
          Reset
        </button>
      </div>
    </div>
  );
}
