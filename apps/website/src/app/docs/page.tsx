import * as React from "react"
import { Separator } from "@/components/ui/separator"

export default function DocsPage() {
  return (
    <div className="space-y-10 pb-16">
      <div className="space-y-4">
        <h1 className="text-4xl font-bold tracking-tight" id="introduction">Introduction</h1>
        <p className="text-lg text-muted-foreground">
          Welcome to the LifeOfPy documentation. Learn how to build beautiful, accessible Python desktop apps.
        </p>
      </div>

      <Separator />

      <div className="space-y-6">
        <p className="leading-7">
          LifeOfPy is not a component library. It's a collection of reusable components that you can copy and paste into your applications.
        </p>
        <p className="leading-7">
          <strong>What do you mean by not a component library?</strong><br/>
          I mean you do not install it as a monolithic dependency. It is not available or distributed via PyPI as a giant module.
        </p>
        <p className="leading-7">
          Pick the components you need. Copy the code into your project and customize to your needs. The code is yours.
        </p>
      </div>

      <div className="space-y-4" id="principles">
        <h2 className="scroll-m-20 border-b pb-2 text-2xl font-semibold tracking-tight">Core Principles</h2>
        <ul className="my-6 ml-6 list-disc [&>li]:mt-2">
          <li><strong>Accessible</strong>: Components follow the best practices for keyboard navigation.</li>
          <li><strong>Customizable</strong>: You own the code. Change everything.</li>
          <li><strong>Open Source</strong>: Built by developers, for developers.</li>
        </ul>
      </div>
      
      <div className="space-y-4" id="faq">
        <h2 className="scroll-m-20 border-b pb-2 text-2xl font-semibold tracking-tight">FAQ</h2>
        <div className="space-y-4 pt-4">
          <h3 className="font-semibold text-lg">Why copy/paste and not a library?</h3>
          <p className="leading-7 text-muted-foreground">
            The idea behind this is to give you ownership and control over the code, allowing you to decide how the components are built and styled. Packaging it in an npm-like equivalent would strip you of that control.
          </p>
        </div>
      </div>
    </div>
  )
}
