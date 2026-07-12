"use client"

import * as React from "react"
import { ComponentShowcase } from "@/components/home/component-showcase"

export default function ComponentsPage() {
  return (
    <div className="space-y-12">
      <div className="space-y-4">
        <h1 className="text-4xl font-bold tracking-tight text-foreground">All Components</h1>
        <p className="text-foreground/50 text-lg max-w-2xl leading-relaxed">
          The definitive library of premium Python UI components. Browse, interact, and install directly into your application.
        </p>
      </div>

      {/* REUSE THE EDITORIAL GALLERY FROM HOMEPAGE */}
      <ComponentShowcase />
    </div>
  )
}
