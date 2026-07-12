import * as React from "react"
import Link from "next/link"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Search } from "lucide-react"

export default function ComponentsLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="container mx-auto max-w-[1600px] px-4 md:px-8 flex-1 items-start md:grid md:grid-cols-[220px_minmax(0,1fr)] md:gap-6 lg:grid-cols-[260px_minmax(0,1fr)] lg:gap-12 mt-12 mb-24">
      
      {/* LEFT NAVIGATION */}
      <aside className="fixed top-20 z-30 -ml-2 hidden h-[calc(100vh-5rem)] w-full shrink-0 md:sticky md:block overflow-y-auto">
        <ScrollArea className="h-full py-6 pr-6 lg:py-2">
          
          {/* SEARCH */}
          <div className="relative mb-8 group">
            <Search className="absolute left-3 top-2.5 h-4 w-4 text-foreground/40 group-focus-within:text-foreground/80 transition-colors" />
            <input 
              type="text" 
              placeholder="Search components..." 
              className="w-full h-9 rounded-lg border border-black/10 dark:border-white/10 bg-black/[0.02] dark:bg-white/[0.02] pl-9 pr-3 text-sm focus:outline-none focus:ring-2 focus:ring-primary/20 transition-all placeholder:text-foreground/40"
            />
          </div>

          <div className="w-full space-y-8">
            <div>
              <h4 className="mb-2 px-2 text-xs font-semibold uppercase tracking-wider text-foreground/40">Discover</h4>
              <div className="grid grid-flow-row auto-rows-max text-sm space-y-0.5">
                <Link href="/components" className="group flex w-full items-center rounded-lg bg-black/[0.03] dark:bg-white/[0.03] font-medium px-2 py-1.5 text-foreground">
                  All Components
                </Link>
                <Link href="/components?filter=new" className="group flex w-full items-center rounded-lg border border-transparent px-2 py-1.5 hover:bg-black/5 dark:hover:bg-white/5 text-foreground/60 hover:text-foreground transition-colors">
                  Recently Added
                </Link>
                <Link href="/components?filter=popular" className="group flex w-full items-center rounded-lg border border-transparent px-2 py-1.5 hover:bg-black/5 dark:hover:bg-white/5 text-foreground/60 hover:text-foreground transition-colors">
                  Popular
                </Link>
              </div>
            </div>
            
            <div>
              <h4 className="mb-2 px-2 text-xs font-semibold uppercase tracking-wider text-foreground/40">Categories</h4>
              <div className="grid grid-flow-row auto-rows-max text-sm space-y-0.5">
                {['Forms', 'Data Display', 'Feedback', 'Overlays', 'Navigation', 'Layout', 'Utilities'].map(cat => (
                  <Link 
                    key={cat} 
                    href={`/components?category=${cat.toLowerCase()}`} 
                    className="group flex w-full items-center rounded-lg border border-transparent px-2 py-1.5 hover:bg-black/5 dark:hover:bg-white/5 text-foreground/60 hover:text-foreground transition-colors"
                  >
                    {cat}
                  </Link>
                ))}
              </div>
            </div>
          </div>
        </ScrollArea>
      </aside>

      {/* MAIN CONTENT */}
      <main className="relative py-2 lg:py-2">
        <div className="mx-auto w-full min-w-0">
          {children}
        </div>
      </main>
    </div>
  )
}
