// src/components/ResultPanel.tsx
import React from "react";
import EmotionChart from "./EmotionChart";
import RiskCard from "./RiskCard";
import SuggestionsBox from "./SuggestionsBox";

type Emotion = { label: string; score: number };
type Result = {
  emotions: Emotion[];
  text_score: number;
  sleep_score: number;
  risk_value: number;
  risk_level: "low" | "medium" | "high";
  retrieved_context: string[];
  suggestions: string;
};

type Props = {
  result: Result | null;
};

export default function ResultPanel({ result }: Props) {
  if (!result) {
    return (
      <div className="p-6 bg-white rounded-xl shadow text-gray-500">
        Results will appear here after you analyze your text.
      </div>
    );
  }

  const { emotions, risk_level, risk_value, suggestions, text_score, sleep_score } = result;

  // ensure values are valid
  const safeRiskLevel: "low" | "medium" | "high" = (["low", "medium", "high"].includes(risk_level) ? risk_level : "low") as any;
  const safeRiskValue = typeof risk_value === "number" ? risk_value : 0;

  return (
    <div className="space-y-6">
      <div className="grid md:grid-cols-3 gap-6">
        <div className="md:col-span-1">
          <RiskCard level={safeRiskLevel} value={safeRiskValue} />
          <div className="mt-4 p-4 bg-white rounded shadow">
            <div className="text-sm text-gray-500">Text health score</div>
            <div className="text-xl font-semibold">{Math.round(text_score * 100)}%</div>
            <div className="text-xs text-gray-400 mt-2">Sleep score: {Math.round(sleep_score * 100)}%</div>
          </div>
        </div>

        <div className="md:col-span-2 space-y-4">
          <div className="p-4 bg-white rounded shadow">
            <h4 className="font-semibold mb-3">Emotion Breakdown</h4>
            <EmotionChart emotions={emotions} />
          </div>

          <div>
            <SuggestionsBox suggestions={suggestions} />
          </div>
        </div>
      </div>
    </div>
  );
}
