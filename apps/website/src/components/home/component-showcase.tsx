"use client"

import * as React from "react"
import { motion, AnimatePresence } from "framer-motion"
import { 
  Calendar, ChevronRight, Check, Search, Command, 
  CheckCircle2, ChevronDown, Bell, MoreHorizontal, 
  User, Key, LogOut, FileText, ArrowRight, Settings, CreditCard
} from "lucide-react"
import { Badge } from "@/components/ui/badge"

export function ComponentShowcase() {
  const [toastOpen, setToastOpen] = React.useState(false)
  const [tab, setTab] = React.useState("preview")
  const [switchOn, setSwitchOn] = React.useState(false)
  const [checkboxChecked, setCheckboxChecked] = React.useState(false)

  return (
    <div className="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6 pb-20">
      
      {/* 1. LARGE SIDEBAR (Tall) */}
      <motion.div 
        whileHover={{ y: -4 }}
        transition={{ duration: 0.4, ease: "easeOut" }}
        className="break-inside-avoid relative flex flex-col overflow-hidden rounded-[2rem] border border-black/5 dark:border-white/5 bg-white dark:bg-[#111] shadow-sm group"
      >
        <div className="flex flex-1 p-6 h-[400px]">
          <div className="w-full h-full rounded-xl border border-black/5 dark:border-white/5 bg-black/[0.02] dark:bg-white/[0.02] flex flex-col overflow-hidden">
             <div className="px-4 py-3 border-b border-black/5 dark:border-white/5 font-semibold text-sm flex items-center justify-between">
               LifeOfPy
               <ChevronDown className="h-4 w-4 text-foreground/40" />
             </div>
             <div className="p-2 space-y-1">
               <div className="text-[10px] font-medium text-foreground/40 uppercase tracking-wider px-2 py-1">Favorites</div>
               <div className="flex items-center justify-between px-2 py-1.5 text-sm hover:bg-black/5 dark:hover:bg-white/5 rounded-md text-foreground/70 cursor-pointer">
                 <div className="flex items-center"><FileText className="h-4 w-4 mr-2 text-foreground/50" /> Q3 Planning</div>
               </div>
               <div className="flex items-center justify-between px-2 py-1.5 text-sm bg-black/5 dark:bg-white/5 rounded-md font-medium cursor-pointer">
                 <div className="flex items-center"><User className="h-4 w-4 mr-2 text-foreground/50" /> Customers</div>
                 <div className="h-4 w-4 flex items-center justify-center rounded-full bg-blue-500 text-[9px] text-white font-bold">3</div>
               </div>
             </div>
             <div className="mt-auto p-2 border-t border-black/5 dark:border-white/5">
                <div className="flex items-center px-2 py-1.5 text-sm hover:bg-black/5 dark:hover:bg-white/5 rounded-md text-foreground/70 cursor-pointer">
                 <Settings className="h-4 w-4 mr-2 text-foreground/50" /> Settings
               </div>
             </div>
          </div>
        </div>
        <CardFooter title="Sidebar" variant="Layout" />
      </motion.div>

      {/* 2. MEDIUM TABLE (Wide) */}
      <motion.div 
        whileHover={{ y: -4 }}
        transition={{ duration: 0.4, ease: "easeOut" }}
        className="break-inside-avoid relative flex flex-col overflow-hidden rounded-[2rem] border border-black/5 dark:border-white/5 bg-white dark:bg-[#111] shadow-sm group"
      >
        <div className="flex flex-1 p-6 h-[300px]">
          <div className="w-full h-full rounded-xl border border-black/5 dark:border-white/5 overflow-hidden flex flex-col">
            <div className="px-4 py-2 border-b border-black/5 dark:border-white/5 flex items-center">
              <Search className="h-3.5 w-3.5 text-foreground/40 mr-2" />
              <input type="text" placeholder="Filter emails..." className="text-sm bg-transparent outline-none placeholder:text-foreground/30 flex-1" />
            </div>
            <table className="w-full text-sm">
              <thead className="bg-black/[0.02] dark:bg-white/[0.02] border-b border-black/5 dark:border-white/5">
                <tr>
                  <th className="px-4 py-2 text-left font-medium text-foreground/60 w-8"><div className="h-3 w-3 rounded border border-black/20 dark:border-white/20" /></th>
                  <th className="px-4 py-2 text-left font-medium text-foreground/60">Email</th>
                  <th className="px-4 py-2 text-right font-medium text-foreground/60">Role</th>
                </tr>
              </thead>
              <tbody>
                {[
                  { email: "olivia@example.com", role: "Owner" },
                  { email: "jackson@example.com", role: "Member" },
                  { email: "isabella@example.com", role: "Member" }
                ].map((user, i) => (
                  <tr key={i} className="border-b border-black/5 dark:border-white/5 last:border-0 hover:bg-black/[0.01] dark:hover:bg-white/[0.01]">
                    <td className="px-4 py-2"><div className="h-3 w-3 rounded border border-black/20 dark:border-white/20" /></td>
                    <td className="px-4 py-2 font-medium">{user.email}</td>
                    <td className="px-4 py-2 text-right text-foreground/50">{user.role}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
        <CardFooter title="Table" variant="Data Display" />
      </motion.div>

      {/* 3. SMALL BUTTON (Compact) */}
      <motion.div 
        whileHover={{ y: -4 }}
        transition={{ duration: 0.4, ease: "easeOut" }}
        className="break-inside-avoid relative flex flex-col overflow-hidden rounded-[2rem] border border-black/5 dark:border-white/5 bg-white dark:bg-[#111] shadow-sm group"
      >
        <div className="flex flex-1 p-8 items-center justify-center h-[200px]">
          <button className="h-10 px-6 rounded-full bg-foreground text-background text-sm font-medium shadow-[0_4px_14px_0_rgb(0,0,0,0.1)] hover:scale-[1.02] active:scale-[0.98] transition-all flex items-center space-x-2">
            <span>Continue</span>
            <ArrowRight className="h-4 w-4" />
          </button>
        </div>
        <CardFooter title="Button" variant="Inputs" />
      </motion.div>

      {/* 4. LARGE CALENDAR (Tall) */}
      <motion.div 
        whileHover={{ y: -4 }}
        transition={{ duration: 0.4, ease: "easeOut" }}
        className="break-inside-avoid relative flex flex-col overflow-hidden rounded-[2rem] border border-black/5 dark:border-white/5 bg-white dark:bg-[#111] shadow-sm group"
      >
        <div className="flex flex-1 p-6 items-center justify-center h-[350px]">
          <div className="rounded-xl border border-black/10 dark:border-white/10 p-4 shadow-sm bg-white dark:bg-[#111]">
            <div className="flex items-center justify-between mb-4">
              <ChevronRight className="h-4 w-4 rotate-180 opacity-50" />
              <div className="text-sm font-medium">November 2026</div>
              <ChevronRight className="h-4 w-4 opacity-50" />
            </div>
            <div className="grid grid-cols-7 gap-1 text-center mb-2">
              {['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'].map(d => (
                <div key={d} className="text-[10px] font-medium text-foreground/40 w-8">{d}</div>
              ))}
            </div>
            <div className="grid grid-cols-7 gap-1 text-sm">
              {[...Array(30)].map((_, i) => (
                <div 
                  key={i} 
                  className={`h-8 w-8 flex items-center justify-center rounded-md cursor-pointer transition-colors ${
                    i === 11 ? "bg-foreground text-background font-medium" : "hover:bg-black/5 dark:hover:bg-white/5"
                  }`}
                >
                  {i + 1}
                </div>
              ))}
            </div>
          </div>
        </div>
        <CardFooter title="Calendar" variant="Data Display" />
      </motion.div>

      {/* 5. MEDIUM COMMAND PALETTE (Wide) */}
      <motion.div 
        whileHover={{ y: -4 }}
        transition={{ duration: 0.4, ease: "easeOut" }}
        className="break-inside-avoid relative flex flex-col overflow-hidden rounded-[2rem] border border-black/5 dark:border-white/5 bg-white dark:bg-[#111] shadow-sm group"
      >
        <div className="flex flex-1 p-6 items-center justify-center h-[320px] bg-[radial-gradient(circle_at_center,rgba(0,0,0,0.02)_1px,transparent_1px)] dark:bg-[radial-gradient(circle_at_center,rgba(255,255,255,0.02)_1px,transparent_1px)]" style={{ backgroundSize: '16px 16px' }}>
          <div className="w-full max-w-sm rounded-xl border border-black/10 dark:border-white/10 bg-white dark:bg-[#111] shadow-xl overflow-hidden">
            <div className="flex items-center border-b border-black/5 dark:border-white/5 px-3">
              <Search className="h-4 w-4 text-foreground/40 mr-2" />
              <input type="text" placeholder="Search documentation..." className="h-12 w-full bg-transparent text-sm focus:outline-none placeholder:text-foreground/30" />
              <Badge variant="outline" className="text-[10px] px-1.5 py-0 rounded border-black/10 dark:border-white/10 text-foreground/40 shadow-none">⌘K</Badge>
            </div>
            <div className="p-2 space-y-1">
              <div className="px-2 py-1 text-[10px] font-medium text-foreground/40 uppercase tracking-wider">Suggestions</div>
              <div className="flex items-center justify-between rounded-md px-2 py-2 text-sm hover:bg-black/5 dark:hover:bg-white/5 cursor-pointer bg-black/5 dark:bg-white/5">
                <div className="flex items-center space-x-2">
                  <FileText className="h-4 w-4 text-foreground/60" />
                  <span className="font-medium">Installation Guide</span>
                </div>
              </div>
              <div className="flex items-center justify-between rounded-md px-2 py-2 text-sm hover:bg-black/5 dark:hover:bg-white/5 cursor-pointer">
                <div className="flex items-center space-x-2">
                  <FileText className="h-4 w-4 text-foreground/60" />
                  <span className="text-foreground/80">Theming</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <CardFooter title="Command" variant="Navigation" />
      </motion.div>

      {/* 6. SMALL SWITCH/CHECKBOX (Compact) */}
      <motion.div 
        whileHover={{ y: -4 }}
        transition={{ duration: 0.4, ease: "easeOut" }}
        className="break-inside-avoid relative flex flex-col overflow-hidden rounded-[2rem] border border-black/5 dark:border-white/5 bg-white dark:bg-[#111] shadow-sm group"
      >
        <div className="flex flex-1 p-8 items-center justify-center h-[200px] gap-8">
           {/* Custom switch */}
           <div 
             onClick={() => setSwitchOn(!switchOn)}
             className={`w-11 h-6 rounded-full cursor-pointer relative transition-colors duration-200 ${switchOn ? "bg-foreground" : "bg-black/20 dark:bg-white/20"}`}
           >
             <motion.div 
               animate={{ x: switchOn ? 22 : 2 }}
               transition={{ type: "spring", stiffness: 500, damping: 30 }}
               className="w-5 h-5 bg-white rounded-full absolute top-[2px] shadow-sm"
             />
           </div>
           
           {/* Custom checkbox */}
           <div 
             onClick={() => setCheckboxChecked(!checkboxChecked)}
             className={`w-5 h-5 rounded cursor-pointer flex items-center justify-center transition-colors duration-200 border ${checkboxChecked ? "bg-foreground border-foreground text-background" : "bg-transparent border-black/20 dark:border-white/20"}`}
           >
             {checkboxChecked && <Check className="h-3.5 w-3.5" />}
           </div>
        </div>
        <CardFooter title="Toggle & Checkbox" variant="Inputs" />
      </motion.div>

      {/* 7. MEDIUM TABS (Wide) */}
      <motion.div 
        whileHover={{ y: -4 }}
        transition={{ duration: 0.4, ease: "easeOut" }}
        className="break-inside-avoid relative flex flex-col overflow-hidden rounded-[2rem] border border-black/5 dark:border-white/5 bg-white dark:bg-[#111] shadow-sm group"
      >
        <div className="flex flex-1 p-6 items-center justify-center h-[250px]">
          <div className="w-full max-w-sm rounded-xl p-1 bg-black/5 dark:bg-white/5 flex relative">
            {["preview", "code", "settings"].map((t) => (
              <button
                key={t}
                onClick={() => setTab(t)}
                className={`relative flex-1 py-1.5 text-sm font-medium transition-colors z-10 capitalize ${
                  tab === t ? "text-foreground" : "text-foreground/50 hover:text-foreground/80"
                }`}
              >
                {t}
                {tab === t && (
                  <motion.div
                    layoutId="active-tab"
                    className="absolute inset-0 bg-white dark:bg-[#222] rounded-lg shadow-sm -z-10"
                    transition={{ type: "spring", stiffness: 400, damping: 30 }}
                  />
                )}
              </button>
            ))}
          </div>
        </div>
        <CardFooter title="Tabs" variant="Navigation" />
      </motion.div>

      {/* 8. SMALL TOAST (Compact) */}
      <motion.div 
        whileHover={{ y: -4 }}
        transition={{ duration: 0.4, ease: "easeOut" }}
        className="break-inside-avoid relative flex flex-col overflow-hidden rounded-[2rem] border border-black/5 dark:border-white/5 bg-white dark:bg-[#111] shadow-sm group"
      >
        <div className="flex flex-1 flex-col items-center justify-center p-8 relative h-[250px]">
          <button 
            onClick={() => setToastOpen(true)}
            className="text-xs font-medium underline underline-offset-4 text-foreground/50 hover:text-foreground mb-4"
          >
            Trigger Toast
          </button>
          
          <AnimatePresence>
            {toastOpen && (
              <motion.div
                initial={{ opacity: 0, y: 10, scale: 0.95 }}
                animate={{ opacity: 1, y: 0, scale: 1 }}
                exit={{ opacity: 0, scale: 0.95 }}
                onAnimationComplete={() => setTimeout(() => setToastOpen(false), 2000)}
                className="absolute bottom-8 w-[85%] rounded-xl border border-black/5 dark:border-white/10 bg-white dark:bg-[#222] shadow-xl p-3 flex gap-3"
              >
                <CheckCircle2 className="h-5 w-5 text-green-500 shrink-0" />
                <div className="flex flex-col">
                  <span className="text-sm font-semibold">Message sent</span>
                  <span className="text-[11px] text-foreground/50">Anyone with the link can view.</span>
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
        <CardFooter title="Toast" variant="Feedback" />
      </motion.div>

      {/* 9. MEDIUM ACCORDION (Wide) */}
      <motion.div 
        whileHover={{ y: -4 }}
        transition={{ duration: 0.4, ease: "easeOut" }}
        className="break-inside-avoid relative flex flex-col overflow-hidden rounded-[2rem] border border-black/5 dark:border-white/5 bg-white dark:bg-[#111] shadow-sm group"
      >
        <div className="flex flex-1 p-6 items-center justify-center h-[300px]">
           <div className="w-full max-w-sm border border-black/5 dark:border-white/5 rounded-xl divide-y divide-black/5 dark:divide-white/5">
             <div className="p-4 flex items-center justify-between cursor-pointer group">
               <span className="text-sm font-medium">Is it accessible?</span>
               <ChevronDown className="h-4 w-4 text-foreground/40 group-hover:text-foreground transition-colors rotate-180" />
             </div>
             <div className="p-4 text-sm text-foreground/60 bg-black/[0.01] dark:bg-white/[0.01]">
               Yes. It adheres to the WAI-ARIA design pattern and supports keyboard navigation.
             </div>
             <div className="p-4 flex items-center justify-between cursor-pointer group">
               <span className="text-sm font-medium">Is it styled?</span>
               <ChevronDown className="h-4 w-4 text-foreground/40 group-hover:text-foreground transition-colors" />
             </div>
           </div>
        </div>
        <CardFooter title="Accordion" variant="Data Display" />
      </motion.div>

      {/* 10. LARGE DIALOG (Tall) */}
      <motion.div 
        whileHover={{ y: -4 }}
        transition={{ duration: 0.4, ease: "easeOut" }}
        className="break-inside-avoid relative flex flex-col overflow-hidden rounded-[2rem] border border-black/5 dark:border-white/5 bg-white dark:bg-[#111] shadow-sm group"
      >
        <div className="flex flex-1 p-6 items-center justify-center h-[400px]">
          <div className="w-full rounded-2xl border border-black/10 dark:border-white/10 bg-white dark:bg-[#111] shadow-2xl p-6 relative overflow-hidden">
             <div className="space-y-1 mb-6">
                <h4 className="text-lg font-semibold text-foreground">Edit Profile</h4>
                <p className="text-sm text-foreground/50">Make changes to your profile here.</p>
             </div>
             <div className="space-y-4">
                <div className="space-y-1.5">
                  <label className="text-xs font-medium text-foreground/70">Name</label>
                  <input type="text" defaultValue="Aashir Zayd" className="w-full h-9 rounded-lg border border-black/10 dark:border-white/10 bg-transparent px-3 text-sm focus:outline-none focus:ring-2 focus:ring-primary/20" />
                </div>
                <div className="space-y-1.5">
                  <label className="text-xs font-medium text-foreground/70">Username</label>
                  <input type="text" defaultValue="@aashir" className="w-full h-9 rounded-lg border border-black/10 dark:border-white/10 bg-transparent px-3 text-sm focus:outline-none focus:ring-2 focus:ring-primary/20" />
                </div>
             </div>
             <div className="mt-8 flex justify-end space-x-2">
                <button className="h-9 px-4 rounded-lg bg-transparent text-sm font-medium">Cancel</button>
                <button className="h-9 px-4 rounded-lg bg-foreground text-background text-sm font-medium shadow-sm">Save changes</button>
             </div>
          </div>
        </div>
        <CardFooter title="Dialog" variant="Overlays" />
      </motion.div>

      {/* 11. SMALL DROPDOWN (Compact) */}
      <motion.div 
        whileHover={{ y: -4 }}
        transition={{ duration: 0.4, ease: "easeOut" }}
        className="break-inside-avoid relative flex flex-col overflow-hidden rounded-[2rem] border border-black/5 dark:border-white/5 bg-white dark:bg-[#111] shadow-sm group"
      >
        <div className="flex flex-1 p-6 items-center justify-center h-[280px]">
          <div className="w-56 rounded-xl border border-black/10 dark:border-white/10 bg-white dark:bg-[#111] shadow-xl p-1.5 flex flex-col">
            <div className="text-xs font-medium text-foreground/40 px-2 py-1.5">My Account</div>
            <div className="flex items-center justify-between px-2 py-1.5 rounded-md hover:bg-black/5 dark:hover:bg-white/5 cursor-pointer group/item">
              <span className="text-sm flex items-center"><User className="h-4 w-4 mr-2 opacity-60" /> Profile</span>
              <span className="text-[10px] text-foreground/40 font-mono opacity-0 group-hover/item:opacity-100 transition-opacity">⇧⌘P</span>
            </div>
            <div className="flex items-center justify-between px-2 py-1.5 rounded-md hover:bg-black/5 dark:hover:bg-white/5 cursor-pointer">
              <span className="text-sm flex items-center"><CreditCard className="h-4 w-4 mr-2 opacity-60" /> Billing</span>
            </div>
            <div className="flex items-center justify-between px-2 py-1.5 rounded-md hover:bg-black/5 dark:hover:bg-white/5 cursor-pointer">
              <span className="text-sm flex items-center"><Settings className="h-4 w-4 mr-2 opacity-60" /> Settings</span>
            </div>
            <div className="h-px w-full bg-black/5 dark:bg-white/5 my-1" />
            <div className="flex items-center px-2 py-1.5 rounded-md hover:bg-red-500/10 text-red-600 dark:text-red-400 cursor-pointer">
              <span className="text-sm flex items-center"><LogOut className="h-4 w-4 mr-2 opacity-60" /> Log out</span>
            </div>
          </div>
        </div>
        <CardFooter title="Dropdown" variant="Overlays" />
      </motion.div>

      {/* 12. SMALL INPUT (Compact) */}
      <motion.div 
        whileHover={{ y: -4 }}
        transition={{ duration: 0.4, ease: "easeOut" }}
        className="break-inside-avoid relative flex flex-col overflow-hidden rounded-[2rem] border border-black/5 dark:border-white/5 bg-white dark:bg-[#111] shadow-sm group"
      >
        <div className="flex flex-1 flex-col items-center justify-center p-8 h-[200px]">
          <div className="w-full space-y-1.5 relative">
            <input 
              type="text" 
              placeholder="Filter projects..."
              className="w-full h-10 rounded-lg border border-black/10 dark:border-white/10 bg-transparent pl-9 pr-3 text-sm focus:outline-none focus:ring-2 focus:ring-primary/20 transition-all"
            />
            <Search className="absolute left-3 top-2.5 h-4 w-4 text-foreground/40" />
          </div>
        </div>
        <CardFooter title="Input" variant="Inputs" />
      </motion.div>

    </div>
  )
}

function CardFooter({ title, variant }: { title: string, variant: string }) {
  return (
    <div className="border-t border-black/5 dark:border-white/5 bg-black/[0.01] dark:bg-white/[0.01] px-6 py-4 flex justify-between items-center group-hover:bg-black/[0.02] dark:group-hover:bg-white/[0.02] transition-colors">
      <div className="flex items-center space-x-2">
        <span className="font-semibold text-sm">{title}</span>
        <Badge variant="secondary" className="text-[9px] bg-black/5 dark:bg-white/10 tracking-widest uppercase">{variant}</Badge>
      </div>
      <motion.div 
        className="text-xs font-medium flex items-center opacity-0 group-hover:opacity-100 -translate-x-2 group-hover:translate-x-0 transition-all text-foreground/60 hover:text-foreground cursor-pointer"
      >
        Open Component <ArrowRight className="h-3 w-3 ml-1" />
      </motion.div>
    </div>
  )
}
