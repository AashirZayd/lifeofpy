"use client"

import * as React from "react"
import { motion, AnimatePresence } from "framer-motion"
import { Check, Search, Calendar, CreditCard, Settings, User, Bell, Download, ChevronRight, X } from "lucide-react"

export function HeroExplorer() {
  const [step, setStep] = React.useState(0)

  React.useEffect(() => {
    const timer = setInterval(() => {
      setStep((prev) => (prev < 6 ? prev + 1 : 0))
    }, 1500) // Slower pacing to let the user see the assembly
    return () => clearInterval(timer)
  }, [])

  return (
    <div className="relative mx-auto w-full max-w-6xl mt-12 grid grid-cols-1 lg:grid-cols-2 gap-8 items-center perspective-[2000px]">
      
      {/* LEFT: CLI INSTALLATION */}
      <motion.div
        initial={{ opacity: 0, x: -30 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
        className="relative flex flex-col overflow-hidden rounded-2xl border border-black/10 dark:border-white/10 bg-[#0a0a0a] shadow-[0_20px_60px_rgba(0,0,0,0.15)] h-[440px] z-10"
      >
        <div className="flex items-center px-4 py-3 border-b border-white/10 bg-white/[0.02]">
          <div className="flex space-x-2">
            <div className="h-3 w-3 rounded-full bg-white/20" />
            <div className="h-3 w-3 rounded-full bg-white/20" />
            <div className="h-3 w-3 rounded-full bg-white/20" />
          </div>
          <div className="mx-auto text-[11px] font-medium text-white/40 font-mono tracking-wider">TERMINAL</div>
        </div>
        
        <div className="p-6 font-mono text-[13px] leading-relaxed text-white/80 space-y-4 flex-1">
          <div className="flex items-center space-x-3">
            <span className="text-zinc-500">~</span>
            <span className="text-indigo-400">❯</span>
            <span className="text-white">uvx lifeofpy add</span>
          </div>
          
          <div className="pl-6 space-y-2">
            <AnimateCheck step={step} threshold={1} label="sidebar" path="components/ui/sidebar.py" />
            <AnimateCheck step={step} threshold={2} label="toolbar" path="components/ui/toolbar.py" />
            <AnimateCheck step={step} threshold={3} label="table" path="components/ui/table.py" />
            <AnimateCheck step={step} threshold={4} label="button" path="components/ui/button.py" />
            <AnimateCheck step={step} threshold={5} label="dialog" path="components/ui/dialog.py" />
            
            {step >= 6 && (
              <motion.div 
                initial={{ opacity: 0 }} animate={{ opacity: 1 }}
                className="mt-4 pt-4 border-t border-white/10 text-green-400 flex items-center"
              >
                ✓ 5 components installed successfully.
              </motion.div>
            )}
          </div>
        </div>
      </motion.div>

      {/* RIGHT: COMPONENT ASSEMBLY */}
      <div className="relative h-[440px] w-full rounded-2xl border border-black/10 dark:border-white/10 bg-white dark:bg-[#111] shadow-[0_30px_100px_rgba(0,0,0,0.12)] overflow-hidden flex">
        
        {/* 1. SIDEBAR (Appears at step 1) */}
        <motion.div 
          initial={{ x: -200 }}
          animate={{ x: step >= 1 ? 0 : -200 }}
          transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
          className="w-48 border-r border-black/5 dark:border-white/5 bg-black/[0.02] dark:bg-white/[0.02] flex flex-col h-full absolute left-0 top-0 bottom-0 z-10"
        >
          <div className="p-4 border-b border-black/5 dark:border-white/5 font-semibold text-sm">LifeOfPy</div>
          <div className="p-2 space-y-1">
            <div className="flex items-center px-2 py-1.5 text-sm bg-black/5 dark:bg-white/5 rounded-md font-medium"><CreditCard className="h-4 w-4 mr-2 opacity-50" /> Billing</div>
            <div className="flex items-center px-2 py-1.5 text-sm hover:bg-black/5 dark:hover:bg-white/5 rounded-md text-foreground/70"><User className="h-4 w-4 mr-2 opacity-50" /> Account</div>
            <div className="flex items-center px-2 py-1.5 text-sm hover:bg-black/5 dark:hover:bg-white/5 rounded-md text-foreground/70"><Settings className="h-4 w-4 mr-2 opacity-50" /> Settings</div>
          </div>
        </motion.div>

        {/* MAIN CONTENT AREA */}
        <div className="flex-1 ml-48 flex flex-col h-full bg-white dark:bg-[#111] relative z-0">
          
          {/* 2. TOOLBAR (Appears at step 2) */}
          <motion.div
            initial={{ y: -50, opacity: 0 }}
            animate={{ y: step >= 2 ? 0 : -50, opacity: step >= 2 ? 1 : 0 }}
            transition={{ duration: 0.4, ease: "easeOut" }}
            className="h-14 border-b border-black/5 dark:border-white/5 flex items-center justify-between px-4"
          >
            <div className="text-sm font-medium">Invoices</div>
            <div className="flex items-center space-x-2">
              <div className="relative">
                <Search className="absolute left-2.5 top-2 h-3.5 w-3.5 text-foreground/40" />
                <div className="h-7 w-40 rounded-md border border-black/10 dark:border-white/10 bg-black/[0.02] dark:bg-white/[0.02]" />
              </div>
            </div>
          </motion.div>

          {/* 3. TABLE (Appears at step 3) */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: step >= 3 ? 1 : 0 }}
            transition={{ duration: 0.5 }}
            className="p-4"
          >
            <div className="rounded-lg border border-black/5 dark:border-white/5 overflow-hidden">
              <table className="w-full text-sm">
                <thead className="bg-black/[0.02] dark:bg-white/[0.02] border-b border-black/5 dark:border-white/5">
                  <tr>
                    <th className="px-4 py-2 text-left font-medium text-foreground/60">Invoice</th>
                    <th className="px-4 py-2 text-left font-medium text-foreground/60">Status</th>
                    <th className="px-4 py-2 text-right font-medium text-foreground/60">Amount</th>
                  </tr>
                </thead>
                <tbody>
                  {[1, 2, 3].map((i) => (
                    <tr key={i} className="border-b border-black/5 dark:border-white/5 last:border-0">
                      <td className="px-4 py-2 font-medium">INV-{1000 + i}</td>
                      <td className="px-4 py-2"><span className="inline-flex items-center rounded-full bg-green-500/10 px-2 py-0.5 text-xs font-medium text-green-600 dark:text-green-400">Paid</span></td>
                      <td className="px-4 py-2 text-right text-foreground/70">$250.00</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {/* 4. BUTTONS (Appears at step 4) */}
            <motion.div
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: step >= 4 ? 1 : 0, y: step >= 4 ? 0 : 10 }}
              transition={{ duration: 0.4 }}
              className="mt-4 flex justify-end space-x-2"
            >
              <div className="h-8 px-3 rounded-md border border-black/10 dark:border-white/10 bg-transparent flex items-center text-xs font-medium text-foreground/70">Export</div>
              <div className="h-8 px-3 rounded-md bg-foreground text-background flex items-center text-xs font-medium shadow-sm">Create Invoice</div>
            </motion.div>
          </motion.div>
          
          {/* 5. DIALOG OVERLAY (Appears at step 5) */}
          <AnimatePresence>
            {step >= 5 && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="absolute inset-0 z-50 flex items-center justify-center bg-white/50 dark:bg-black/50 backdrop-blur-sm"
              >
                <motion.div
                  initial={{ scale: 0.95, y: 10, opacity: 0 }}
                  animate={{ scale: 1, y: 0, opacity: 1 }}
                  transition={{ type: "spring", stiffness: 400, damping: 30 }}
                  className="w-80 rounded-xl border border-black/10 dark:border-white/10 bg-white dark:bg-[#111] shadow-2xl overflow-hidden"
                >
                  <div className="p-4 border-b border-black/5 dark:border-white/5 flex justify-between items-center">
                    <h3 className="font-semibold text-sm">Create Invoice</h3>
                    <X className="h-4 w-4 text-foreground/40" />
                  </div>
                  <div className="p-4 space-y-3">
                    <div className="space-y-1">
                      <div className="h-3 w-16 bg-black/10 dark:bg-white/10 rounded" />
                      <div className="h-8 w-full bg-black/5 dark:bg-white/5 rounded border border-black/5 dark:border-white/5" />
                    </div>
                    <div className="space-y-1">
                      <div className="h-3 w-20 bg-black/10 dark:bg-white/10 rounded" />
                      <div className="h-8 w-full bg-black/5 dark:bg-white/5 rounded border border-black/5 dark:border-white/5" />
                    </div>
                  </div>
                  <div className="p-4 border-t border-black/5 dark:border-white/5 bg-black/[0.02] dark:bg-white/[0.02] flex justify-end space-x-2">
                    <div className="h-8 px-3 rounded-md border border-black/10 dark:border-white/10 bg-transparent flex items-center text-xs font-medium">Cancel</div>
                    <div className="h-8 px-3 rounded-md bg-foreground text-background flex items-center text-xs font-medium">Save</div>
                  </div>
                </motion.div>
              </motion.div>
            )}
          </AnimatePresence>

        </div>
      </div>
    </div>
  )
}

function AnimateCheck({ step, threshold, label, path }: { step: number, threshold: number, label: string, path: string }) {
  return (
    <motion.div
      initial={{ opacity: 0, height: 0 }}
      animate={{ opacity: step >= threshold ? 1 : 0, height: step >= threshold ? "auto" : 0 }}
      transition={{ duration: 0.3 }}
      className="flex flex-col space-y-1 overflow-hidden"
    >
      <div className="flex items-center space-x-2 py-1">
        <span className="text-white">{label}</span>
      </div>
      <div className="flex items-center space-x-2 pb-2">
        <Check className="h-3.5 w-3.5 text-green-400" />
        <span className="text-[10px] text-white/40">Created {path}</span>
      </div>
    </motion.div>
  )
}
