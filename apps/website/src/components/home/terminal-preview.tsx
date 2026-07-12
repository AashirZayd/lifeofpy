"use client"

import * as React from "react"
import { motion, AnimatePresence } from "framer-motion"
import { Copy, Check } from "lucide-react"

export function TerminalPreview() {
  const [copied, setCopied] = React.useState(false)

  const handleCopy = () => {
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  return (
    <div className="relative mx-auto w-full max-w-2xl">
      {/* SUBTLE GLOW (for light mode) */}
      <div className="absolute -inset-4 rounded-3xl bg-black/5 dark:bg-white/5 blur-2xl" />
      
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.6, ease: "easeOut" }}
        className="relative overflow-hidden rounded-2xl border border-black/10 dark:border-white/10 bg-[#0A0A0A] shadow-[0_30px_100px_rgba(0,0,0,0.2)] backdrop-blur-xl"
      >
        {/* TERMINAL HEADER */}
        <div className="flex items-center justify-between border-b border-white/10 bg-white/[0.02] px-4 py-3">
          <div className="flex space-x-2">
            <div className="h-3 w-3 rounded-full bg-white/20 hover:bg-[#FF5F56] transition-colors" />
            <div className="h-3 w-3 rounded-full bg-white/20 hover:bg-[#FFBD2E] transition-colors" />
            <div className="h-3 w-3 rounded-full bg-white/20 hover:bg-[#27C93F] transition-colors" />
          </div>
          <div className="text-[11px] font-medium tracking-wide text-white/40">bash</div>
          <button 
            onClick={handleCopy}
            className="flex items-center justify-center h-6 w-6 rounded-md hover:bg-white/10 text-white/40 hover:text-white transition-colors"
          >
            {copied ? <Check className="h-3.5 w-3.5" /> : <Copy className="h-3.5 w-3.5" />}
          </button>
        </div>
        
        {/* TERMINAL BODY */}
        <div className="p-6 font-mono text-[13px] leading-relaxed text-white/80">
          <div className="space-y-5">
            {/* Command 1 */}
            <div className="space-y-1.5">
              <div className="flex items-center space-x-3">
                <span className="text-zinc-500">~</span>
                <span className="text-indigo-400">❯</span>
                <span className="text-white">uvx lifeofpy init</span>
              </div>
              <div className="pl-6 text-white/50">
                <div className="flex items-center space-x-2">
                  <span className="text-green-400">✓</span>
                  <span>Initialized LifeOfPy workspace</span>
                </div>
                <div className="flex items-center space-x-2">
                  <span className="text-green-400">✓</span>
                  <span>Generated pyproject.toml</span>
                </div>
              </div>
            </div>

            {/* Command 2 */}
            <div className="space-y-1.5 pt-2">
              <div className="flex items-center space-x-3">
                <span className="text-zinc-500">~</span>
                <span className="text-indigo-400">❯</span>
                <span className="text-white">uvx lifeofpy add button sidebar card</span>
              </div>
              <div className="pl-6 space-y-1.5">
                <div className="flex items-center space-x-3 text-white/40">
                  <div className="h-1 w-24 bg-white/10 rounded-full overflow-hidden">
                    <motion.div 
                      initial={{ width: 0 }}
                      whileInView={{ width: "100%" }}
                      viewport={{ once: true }}
                      transition={{ duration: 1.5, ease: "easeInOut" }}
                      className="h-full bg-indigo-500 rounded-full"
                    />
                  </div>
                  <span className="text-[10px]">Fetching components...</span>
                </div>
                
                <motion.div
                  initial={{ opacity: 0 }}
                  whileInView={{ opacity: 1 }}
                  viewport={{ once: true }}
                  transition={{ delay: 1.5 }}
                  className="space-y-1"
                >
                  <div className="flex items-center space-x-2">
                    <span className="text-green-400">✓</span>
                    <span className="text-white/60">registry/components/button</span>
                  </div>
                  <div className="flex items-center space-x-2">
                    <span className="text-green-400">✓</span>
                    <span className="text-white/60">registry/components/sidebar</span>
                  </div>
                  <div className="flex items-center space-x-2">
                    <span className="text-green-400">✓</span>
                    <span className="text-white/60">registry/components/card</span>
                  </div>
                </motion.div>
              </div>
            </div>
            
            {/* Input Line */}
            <motion.div 
              initial={{ opacity: 0 }}
              whileInView={{ opacity: 1 }}
              viewport={{ once: true }}
              transition={{ delay: 1.8 }}
              className="flex items-center space-x-3 pt-3"
            >
              <span className="text-zinc-500">~</span>
              <span className="text-indigo-400">❯</span>
              <span className="inline-block w-2 h-4 bg-white/80 animate-pulse" />
            </motion.div>
          </div>
        </div>
      </motion.div>
    </div>
  )
}
