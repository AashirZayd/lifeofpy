import * as React from "react"
import Link from "next/link"
import { ScrollArea } from "@/components/ui/scroll-area"

export default function DocsLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="container mx-auto max-w-screen-2xl px-4 md:px-8 flex-1 items-start md:grid md:grid-cols-[220px_minmax(0,1fr)] md:gap-6 lg:grid-cols-[240px_minmax(0,1fr)] lg:gap-10">
      
      {/* LEFT NAVIGATION */}
      <aside className="fixed top-14 z-30 -ml-2 hidden h-[calc(100vh-3.5rem)] w-full shrink-0 md:sticky md:block overflow-y-auto">
        <ScrollArea className="h-full py-6 pr-6 lg:py-8">
          <div className="w-full pb-4">
            <h4 className="mb-1 rounded-md px-2 py-1 text-sm font-semibold">Getting Started</h4>
            <div className="grid grid-flow-row auto-rows-max text-sm">
              <Link href="/docs" className="group flex w-full items-center rounded-md border border-transparent px-2 py-1 hover:underline text-foreground font-medium">Introduction</Link>
              <Link href="/docs/installation" className="group flex w-full items-center rounded-md border border-transparent px-2 py-1 hover:underline text-muted-foreground">Installation</Link>
              <Link href="/docs/theming" className="group flex w-full items-center rounded-md border border-transparent px-2 py-1 hover:underline text-muted-foreground">Theming</Link>
              <Link href="/docs/cli" className="group flex w-full items-center rounded-md border border-transparent px-2 py-1 hover:underline text-muted-foreground">CLI</Link>
            </div>
          </div>
          <div className="w-full pb-4">
            <h4 className="mb-1 rounded-md px-2 py-1 text-sm font-semibold">Architecture</h4>
            <div className="grid grid-flow-row auto-rows-max text-sm">
              <Link href="/docs/manifest" className="group flex w-full items-center rounded-md border border-transparent px-2 py-1 hover:underline text-muted-foreground">Manifest V1</Link>
              <Link href="/docs/engine" className="group flex w-full items-center rounded-md border border-transparent px-2 py-1 hover:underline text-muted-foreground">LifeOfPy Engine</Link>
            </div>
          </div>
        </ScrollArea>
      </aside>
      
      {/* CENTER CONTENT & RIGHT TOC */}
      <main className="relative py-6 lg:gap-10 lg:py-8 xl:grid xl:grid-cols-[1fr_300px]">
        <div className="mx-auto w-full min-w-0">
          {children}
        </div>
        
        {/* RIGHT TABLE OF CONTENTS */}
        <div className="hidden text-sm xl:block">
          <div className="sticky top-16 -mt-10 pt-4">
            <ScrollArea className="pb-10">
              <div className="space-y-2">
                <p className="font-medium">On This Page</p>
                <ul className="m-0 list-none">
                  <li className="mt-0 pt-2"><a href="#introduction" className="inline-block no-underline transition-colors hover:text-foreground text-foreground font-medium">Introduction</a></li>
                  <li className="mt-0 pt-2"><a href="#principles" className="inline-block no-underline transition-colors hover:text-foreground text-muted-foreground">Core Principles</a></li>
                  <li className="mt-0 pt-2"><a href="#faq" className="inline-block no-underline transition-colors hover:text-foreground text-muted-foreground">FAQ</a></li>
                </ul>
              </div>
            </ScrollArea>
          </div>
        </div>
      </main>
    </div>
  )
}
