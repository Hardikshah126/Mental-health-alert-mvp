// src/lib/api.ts
export interface AnalyzePayload {
  user_id: string;
  text: string;
  sleep_hours: number | null;
}

export interface AnalyzeResponse {
  emotions: { label: string; score: number }[];
  text_score: number;
  sleep_score: number;
  risk_value: number;
  risk_level: string;
  retrieved_context: string[];
  suggestions: string;
}

const BASE_URL = "https://mental-health-alert-mvp-1.onrender.com";

/**
 * Calls backend /analyze. Contains console logs to help debug payloads & errors.
 */
export async function analyzeRemote(
  payload: AnalyzePayload
): Promise<AnalyzeResponse> {
  // Debug: show what the frontend is about to send
  console.log("📤 analyzeRemote payload ->", payload);

  try {
    const response = await fetch(`${BASE_URL}/analyze`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const text = await response.text();
      const err = new Error(`Backend error: ${response.status} - ${text}`);
      console.error("⛔ analyzeRemote error ->", err);
      throw err;
    }

    const data = await response.json();
    console.log("📥 analyzeRemote response ->", data);
    return data as AnalyzeResponse;
  } catch (err) {
    console.error("❗ analyzeRemote network/error ->", err);
    throw err;
  }
}
