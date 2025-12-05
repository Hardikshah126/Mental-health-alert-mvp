import { motion } from "framer-motion";
import { AlertTriangle, CheckCircle, AlertCircle } from "lucide-react";

interface RiskCardProps {
  level: "low" | "medium" | "high";
  value: number;
}

const riskConfig = {
  low: {
    icon: CheckCircle,
    label: "Low Risk",
    message: "You seem to be in a stable emotional state today.",
    colorClass: "text-risk-low",
    bgClass: "bg-risk-low/10",
    borderClass: "border-risk-low/30",
  },
  medium: {
    icon: AlertCircle,
    label: "Medium Risk",
    message: "You may be feeling overwhelmed today. Take it easy.",
    colorClass: "text-risk-medium",
    bgClass: "bg-risk-medium/10",
    borderClass: "border-risk-medium/30",
  },
  high: {
    icon: AlertTriangle,
    label: "High Risk",
    message: "Consider reaching out to someone you trust for support.",
    colorClass: "text-risk-high",
    bgClass: "bg-risk-high/10",
    borderClass: "border-risk-high/30",
  },
};

const RiskCard = ({ level, value }: RiskCardProps) => {
  const config = riskConfig[level];
  const Icon = config.icon;

  return (
    <motion.div
      initial={{ opacity: 0, x: -20 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ duration: 0.5 }}
      className={`glass-card p-6 border-2 ${config.borderClass} ${config.bgClass}`}
    >
      <div className="flex items-start gap-4">
        <div className={`p-3 rounded-2xl ${config.bgClass}`}>
          <Icon className={`w-8 h-8 ${config.colorClass}`} />
        </div>
        <div className="flex-1 space-y-2">
          <div className="flex items-center justify-between">
            <h3 className={`text-xl font-semibold ${config.colorClass}`}>
              {config.label}
            </h3>
            <span className={`text-2xl font-bold ${config.colorClass}`}>
              {Math.round(value * 100)}%
            </span>
          </div>
          <p className="text-muted-foreground">{config.message}</p>
        </div>
      </div>
    </motion.div>
  );
};

export default RiskCard;
