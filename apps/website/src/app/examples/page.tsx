import * as React from "react"

export default function ExamplesPage() {
  return (
    <div className="container max-w-screen-2xl mx-auto py-12 px-4 md:px-8 space-y-10">
      <div className="space-y-4">
        <h1 className="text-4xl font-bold tracking-tight">Examples</h1>
        <p className="text-lg text-muted-foreground max-w-2xl">
          Beautifully designed applications showcasing what you can build with LifeOfPy.
          These are conceptual layouts to inspire your next desktop software.
        </p>
      </div>
      <div className="grid gap-8 md:grid-cols-2 xl:grid-cols-3">
        {['VS Code Clone', 'Mail App', 'Spotify Clone', 'Git Client', 'Database Client', 'Settings App', 'File Explorer', 'Terminal'].map((example) => (
          <div key={example} className="group relative rounded-2xl border border-black/10 dark:border-white/10 bg-white dark:bg-[#0a0a0a] overflow-hidden shadow-sm hover:shadow-md transition-shadow">
            <div className="aspect-[4/3] bg-black/[0.02] dark:bg-white/[0.02] border-b border-black/5 dark:border-white/5 flex flex-col items-center justify-center p-6 relative overflow-hidden">
              <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(0,0,0,0.03)_1px,transparent_1px)] dark:bg-[radial-gradient(circle_at_center,rgba(255,255,255,0.03)_1px,transparent_1px)]" style={{ backgroundSize: '16px 16px' }} />
              <div className="z-10 h-10 px-4 rounded-full bg-white dark:bg-[#222] border border-black/5 dark:border-white/10 flex items-center justify-center text-xs font-medium text-foreground/60 shadow-sm opacity-50 group-hover:opacity-100 transition-opacity">
                View Source Code
              </div>
            </div>
            <div className="p-6">
              <h3 className="font-semibold text-lg">{example}</h3>
              <p className="text-sm text-foreground/50 mt-1">A complete {example.toLowerCase()} interface using official components.</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
