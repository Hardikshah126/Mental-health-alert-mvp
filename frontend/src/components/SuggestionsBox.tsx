import { motion } from "framer-motion";
import { Copy, CheckCheck, Lightbulb } from "lucide-react";
import { useState } from "react";

interface SuggestionsBoxProps {
  suggestions: string;
}

const SuggestionsBox = ({ suggestions }: SuggestionsBoxProps) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    await navigator.clipboard.writeText(suggestions);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const suggestionsList = suggestions.split(". ").filter(Boolean);

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay: 0.4 }}
      className="glass-card p-6 space-y-4"
    >
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <Lightbulb className="w-5 h-5 text-accent-peach" />
          <h3 className="text-lg font-semibold text-foreground">
            Gentle Suggestions
          </h3>
        </div>
        <motion.button
          onClick={handleCopy}
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-secondary/80 
                   text-sm font-medium text-foreground/70 hover:bg-secondary transition-colors"
        >
          {copied ? (
            <>
              <CheckCheck className="w-4 h-4 text-risk-low" />
              Copied!
            </>
          ) : (
            <>
              <Copy className="w-4 h-4" />
              Copy
            </>
          )}
        </motion.button>
      </div>

      <div className="space-y-3">
        {suggestionsList.map((suggestion, index) => (
          <motion.div
            key={index}
            initial={{ opacity: 0, x: -10 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.5 + index * 0.1 }}
            className="flex items-start gap-3 p-3 rounded-xl bg-accent-mint/10 border border-accent-mint/20"
          >
            <span className="flex-shrink-0 w-6 h-6 rounded-full bg-accent-mint/20 
                           flex items-center justify-center text-xs font-semibold text-accent-foreground">
              {index + 1}
            </span>
            <p className="text-foreground/80 text-sm leading-relaxed">
              {suggestion.trim().replace(/\.$/, "")}
            </p>
          </motion.div>
        ))}
      </div>
    </motion.div>
  );
};

export default SuggestionsBox;
