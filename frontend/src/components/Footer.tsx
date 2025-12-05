import { motion } from "framer-motion";

const Footer = () => {
  return (
    <motion.footer
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ delay: 0.8, duration: 0.5 }}
      className="w-full py-8 mt-16"
    >
      <div className="text-center">
        <p className="text-sm text-muted-foreground">
          Made with <span className="text-risk-high">❤️</span> by Hardik Shah
        </p>
      </div>
    </motion.footer>
  );
};

export default Footer;
