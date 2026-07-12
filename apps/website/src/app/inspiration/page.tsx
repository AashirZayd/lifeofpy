import * as React from "react"

export default function InspirationPage() {
  return (
    <div className="container max-w-screen-2xl mx-auto py-12 px-4 md:px-8 space-y-10">
      <div className="space-y-4">
        <h1 className="text-4xl font-bold tracking-tight">Inspiration</h1>
        <p className="text-lg text-muted-foreground max-w-2xl">
          A curated gallery of outstanding desktop interfaces.
        </p>
      </div>
      <div className="columns-1 gap-6 sm:columns-2 lg:columns-3 xl:columns-4 space-y-6">
        {[1, 2, 3, 4, 5, 6, 7, 8].map((i) => (
          <div key={i} className="break-inside-avoid group relative rounded-xl border border-border/50 bg-background overflow-hidden transition-colors hover:border-primary/50">
            <div className={`w-full bg-muted/30 flex items-center justify-center p-6 ${i % 2 === 0 ? 'aspect-square' : 'aspect-[3/4]'}`}>
              <span className="text-muted-foreground font-medium text-sm">Inspiration #{i}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
