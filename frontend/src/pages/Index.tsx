// src/pages/Index.tsx
import React, { useState } from "react";
import InputPanel from "@/components/InputPanel";
import ResultPanel from "@/components/ResultPanel";

export default function Index() {
  // shared result state passed from InputPanel -> ResultPanel
  const [result, setResult] = useState<any | null>(null);

  return (
    <main className="min-h-screen bg-gradient-to-b from-slate-50 to-white p-8">
      <div className="max-w-5xl mx-auto space-y-8">
        {/* Header / Hero */}
        <header className="text-center">
          <h1 className="text-3xl font-bold">Mental Health — Early Warning</h1>
          <p className="mt-2 text-gray-600">
            Write how you're feeling below — we'll analyze mood & provide gentle suggestions.
          </p>
        </header>

        {/* Input panel */}
        <section>
          <InputPanel onResult={setResult} />
        </section>

        {/* Result panel */}
        <section>
          <ResultPanel result={result} />
        </section>

        {/* Footer / small note */}
        <footer className="text-center text-xs text-gray-400 mt-8">
          This tool is a prototype for learning and early-warning only — not a substitute for professional help.
        </footer>
      </div>
    </main>
  );
}
