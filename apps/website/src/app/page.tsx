"use client"

import * as React from "react"
import Link from "next/link"
import { motion, Variants } from "framer-motion"
import { ArrowRight, Search, Terminal } from "lucide-react"

import { buttonVariants } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"

import { HeroExplorer } from "@/components/home/hero-explorer"
import { ComponentShowcase } from "@/components/home/component-showcase"

const FADE_UP_ANIMATION_VARIANTS: Variants = {
  hidden: { opacity: 0, y: 15 },
  show: { opacity: 1, y: 0, transition: { type: "tween", ease: "easeOut", duration: 0.8 } },
}

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col items-center bg-background selection:bg-primary/10 relative">
      
      {/* BRAND VISUAL PATTERN: Subtle plus grid across the entire page */}
      <div className="pointer-events-none fixed inset-0 flex justify-center z-[-1] opacity-40">
        <div className="w-full h-full bg-[url('/plus-grid.svg')] bg-[length:32px_32px]" style={{ backgroundImage: 'radial-gradient(circle at center, rgba(0,0,0,0.06) 1px, transparent 1px)', backgroundSize: '32px 32px' }} />
      </div>

      {/* 1. HERO: Progressive Assembly */}
      <section className="relative w-full overflow-hidden border-b border-black/5 dark:border-white/5 py-24 md:py-32">
        <div className="container relative mx-auto max-w-screen-2xl px-4 flex flex-col items-center text-center">
          <motion.div
            initial="hidden"
            animate="show"
            viewport={{ once: true }}
            variants={{ hidden: {}, show: { transition: { staggerChildren: 0.1 } } }}
            className="flex flex-col items-center space-y-6 z-20"
          >
            <motion.h1 
              variants={FADE_UP_ANIMATION_VARIANTS}
              className="max-w-4xl text-5xl font-bold tracking-tight text-foreground sm:text-6xl md:text-7xl lg:text-[5.5rem] leading-[1.05]"
            >
              Ship desktop apps.<br />Without the styling pain.
            </motion.h1>
            <motion.p 
              variants={FADE_UP_ANIMATION_VARIANTS}
              className="max-w-2xl text-lg leading-relaxed text-foreground/50 sm:text-xl font-medium"
            >
              Beautiful, accessible Python UI components for modern desktop frameworks.
            </motion.p>
            
            <motion.div variants={FADE_UP_ANIMATION_VARIANTS} className="flex items-center space-x-4 pt-4">
              <Link href="/components" className={buttonVariants({ size: "lg", className: "h-12 px-8 rounded-full shadow-[0_4px_14px_0_rgb(0,0,0,0.1)] transition-transform hover:scale-[1.02] active:scale-[0.98]" })}>
                Browse Components
              </Link>
              <Link href="/docs" className={buttonVariants({ size: "lg", variant: "outline", className: "h-12 px-8 rounded-full bg-transparent border-black/10 dark:border-white/10 hover:bg-black/5 transition-transform hover:scale-[1.02] active:scale-[0.98]" })}>
                Documentation
              </Link>
            </motion.div>
          </motion.div>

          <HeroExplorer />
        </div>
      </section>

      {/* 2. COMPONENT SEARCH & GALLERY */}
      <section className="container mx-auto max-w-screen-2xl pt-24 px-4 w-full flex flex-col items-center">
        {/* GLOBAL COMPONENT SEARCH */}
        <div className="w-full max-w-3xl mb-16 relative">
          <div className="absolute -inset-1 rounded-2xl bg-gradient-to-r from-primary/10 via-primary/5 to-transparent blur-lg opacity-50" />
          <div className="relative flex items-center h-16 w-full rounded-2xl border border-black/10 dark:border-white/10 bg-white/80 dark:bg-black/80 backdrop-blur-xl shadow-sm overflow-hidden px-4 transition-shadow hover:shadow-md focus-within:shadow-md focus-within:ring-2 focus-within:ring-primary/20">
            <Search className="h-5 w-5 text-foreground/40 mr-3 shrink-0" />
            <input 
              type="text" 
              placeholder="Search components (e.g. Button, Table, Toast)..." 
              className="flex-1 h-full bg-transparent text-base placeholder:text-foreground/40 focus:outline-none"
            />
            <div className="flex items-center space-x-1 border border-black/10 dark:border-white/10 rounded-md px-1.5 py-0.5 bg-black/[0.02] dark:bg-white/[0.02]">
              <span className="text-[10px] font-mono text-foreground/50">⌘</span>
              <span className="text-[10px] font-mono text-foreground/50">K</span>
            </div>
          </div>
        </div>

        {/* EDITORIAL MASONRY GALLERY */}
        <div className="w-full">
          <div className="mb-12 flex items-center justify-between border-b border-black/5 dark:border-white/5 pb-4">
            <h2 className="text-xl font-semibold tracking-tight text-foreground">Featured Components</h2>
            <Link href="/components" className="text-sm font-medium text-foreground/60 hover:text-foreground flex items-center">
              View all 45+ components <ArrowRight className="h-3 w-3 ml-1" />
            </Link>
          </div>
          <ComponentShowcase />
        </div>
      </section>

      {/* 3. INSTALLATION */}
      <section className="w-full border-t border-black/5 dark:border-white/5 bg-black/[0.01] dark:bg-white/[0.01] py-32 overflow-hidden">
        <div className="container mx-auto max-w-screen-2xl px-4 flex flex-col items-center text-center space-y-8">
          <div className="h-16 w-16 rounded-2xl border border-black/10 dark:border-white/10 bg-white dark:bg-[#111] shadow-lg flex items-center justify-center mb-4">
            <Terminal className="h-8 w-8 text-foreground/80" />
          </div>
          <h2 className="relative text-3xl font-bold tracking-tight text-foreground sm:text-5xl">Start building.</h2>
          <p className="relative max-w-2xl text-foreground/50 sm:text-xl leading-relaxed">
            Install components directly into your project via the CLI. No heavy dependencies, no locked-in architectures. Just pure Python UI.
          </p>
          <div className="mt-8 flex items-center space-x-2 bg-black dark:bg-white text-white dark:text-black rounded-lg p-1 pr-4 shadow-xl">
            <div className="px-4 font-mono text-sm">pip install lifeofpy</div>
            <button className="text-xs font-medium uppercase tracking-wider text-white/50 hover:text-white transition-colors">Copy</button>
          </div>
        </div>
      </section>

    </div>
  )
}
