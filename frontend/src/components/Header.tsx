import { motion } from "framer-motion";
import { Heart, Shield } from "lucide-react";

const Header = () => {
  return (
    <motion.header
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, ease: "easeOut" }}
      className="w-full py-6 px-4 sm:px-8"
    >
      <div className="max-w-4xl mx-auto flex items-center justify-between">
        {/* Logo & Title */}
        <div className="flex items-center gap-3">
          <div className="relative w-10 h-10 flex items-center justify-center">
            <Shield className="w-10 h-10 text-primary absolute" strokeWidth={1.5} />
            <Heart className="w-5 h-5 text-accent-mint absolute" fill="currentColor" />
          </div>
          <div>
            <h1 className="text-xl sm:text-2xl font-semibold text-foreground tracking-tight">
              MindGuard AI
            </h1>
            <p className="text-xs sm:text-sm text-muted-foreground">
              Understand your emotions with gentle insights
            </p>
          </div>
        </div>

        {/* Prototype Badge */}
        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.3, duration: 0.4 }}
          className="px-3 py-1.5 rounded-full bg-accent-peach/30 border border-accent-peach/50"
        >
          <span className="text-xs font-medium text-foreground/70">Prototype UI</span>
        </motion.div>
      </div>
    </motion.header>
  );
};

export default Header;
