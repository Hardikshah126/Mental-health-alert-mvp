import { motion } from "framer-motion";

interface Emotion {
  label: string;
  score: number;
}

interface EmotionChartProps {
  emotions: Emotion[];
}

const emotionColors: Record<string, string> = {
  sadness: "bg-primary",
  anger: "bg-risk-high",
  joy: "bg-accent-mint",
  fear: "bg-accent-peach",
  surprise: "bg-risk-medium",
  disgust: "bg-muted-foreground",
  love: "bg-risk-low",
};

const EmotionChart = ({ emotions }: EmotionChartProps) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay: 0.2 }}
      className="glass-card p-6 space-y-5"
    >
      <h3 className="text-lg font-semibold text-foreground">Emotion Breakdown</h3>
      <div className="space-y-4">
        {emotions.map((emotion, index) => (
          <div key={emotion.label} className="space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-sm font-medium text-foreground/80 capitalize">
                {emotion.label}
              </span>
              <span className="text-sm font-semibold text-muted-foreground">
                {Math.round(emotion.score * 100)}%
              </span>
            </div>
            <div className="h-3 bg-secondary rounded-full overflow-hidden">
              <motion.div
                initial={{ width: 0 }}
                animate={{ width: `${emotion.score * 100}%` }}
                transition={{
                  duration: 0.8,
                  delay: 0.3 + index * 0.1,
                  ease: "easeOut",
                }}
                className={`h-full rounded-full ${emotionColors[emotion.label] || "bg-primary"}`}
              />
            </div>
          </div>
        ))}
      </div>
    </motion.div>
  );
};

export default EmotionChart;
