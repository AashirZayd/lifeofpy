"use client"

import * as React from "react"
import Link from "next/link"

export function Footer() {
  return (
    <footer className="border-t border-border/40 py-6 md:py-0">
      <div className="container mx-auto flex max-w-screen-2xl flex-col items-center justify-between gap-4 px-4 md:h-24 md:flex-row md:px-8">
        <div className="flex flex-col items-center gap-4 px-8 md:flex-row md:gap-2 md:px-0">
          <p className="text-center text-sm leading-loose text-muted-foreground md:text-left">
            Built by{" "}
            <a
              href="https://github.com/LifeOfPy"
              target="_blank"
              rel="noreferrer"
              className="font-medium underline underline-offset-4"
            >
              LifeOfPy
            </a>
            . The source code is available on{" "}
            <a
              href="https://github.com/LifeOfPy/lifeofpy"
              target="_blank"
              rel="noreferrer"
              className="font-medium underline underline-offset-4"
            >
              GitHub
            </a>
            .
          </p>
        </div>
        <div className="flex gap-4 text-sm text-muted-foreground">
          <Link href="/docs" className="hover:underline underline-offset-4">
            Documentation
          </Link>
          <Link href="/roadmap" className="hover:underline underline-offset-4">
            Roadmap
          </Link>
          <Link href="/contributing" className="hover:underline underline-offset-4">
            Contributing
          </Link>
          <Link href="/community" className="hover:underline underline-offset-4">
            Community
          </Link>
        </div>
      </div>
    </footer>
  )
}
