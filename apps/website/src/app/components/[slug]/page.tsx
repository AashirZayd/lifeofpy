"use client"

import * as React from "react"
import { useParams } from "next/navigation"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Separator } from "@/components/ui/separator"
import { Button } from "@/components/ui/button"
import { Check, Copy } from "lucide-react"

export default function ComponentDetailPage() {
  const params = useParams()
  const slug = params.slug as string || "Component"
  const name = slug.charAt(0).toUpperCase() + slug.slice(1).replace("-", " ")

  const [copied, setCopied] = React.useState(false)

  const handleCopy = () => {
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  return (
    <div className="space-y-12 pb-24">
      {/* HEADER */}
      <div className="space-y-4">
        <h1 className="text-4xl font-bold tracking-tight capitalize text-foreground sm:text-5xl">{name}</h1>
        <p className="text-lg text-foreground/50 max-w-2xl">
          A beautifully crafted {name.toLowerCase()} component. Supports multiple variants, sizes, and states out of the box.
        </p>
      </div>

      {/* PREVIEW TABS */}
      <Tabs defaultValue="preview" className="relative mt-8 w-full">
        <div className="flex items-center justify-between pb-4 border-b border-black/5 dark:border-white/5 overflow-x-auto hide-scrollbar">
          <TabsList className="justify-start rounded-none bg-transparent p-0 flex space-x-6">
            <TabsTrigger
              value="preview"
              className="relative rounded-none border-b-2 border-b-transparent bg-transparent px-2 pb-3 pt-2 font-medium text-foreground/50 shadow-none transition-none data-[state=active]:border-b-foreground data-[state=active]:text-foreground data-[state=active]:shadow-none hover:text-foreground"
            >
              Preview
            </TabsTrigger>
            <TabsTrigger
              value="python"
              className="relative rounded-none border-b-2 border-b-transparent bg-transparent px-2 pb-3 pt-2 font-medium text-foreground/50 shadow-none transition-none data-[state=active]:border-b-foreground data-[state=active]:text-foreground data-[state=active]:shadow-none hover:text-foreground"
            >
              Python Reference
            </TabsTrigger>
            <TabsTrigger
              value="react"
              className="relative rounded-none border-b-2 border-b-transparent bg-transparent px-2 pb-3 pt-2 font-medium text-foreground/50 shadow-none transition-none data-[state=active]:border-b-foreground data-[state=active]:text-foreground data-[state=active]:shadow-none hover:text-foreground"
            >
              React Parity
            </TabsTrigger>
            <TabsTrigger
              value="a11y"
              className="relative rounded-none border-b-2 border-b-transparent bg-transparent px-2 pb-3 pt-2 font-medium text-foreground/50 shadow-none transition-none data-[state=active]:border-b-foreground data-[state=active]:text-foreground data-[state=active]:shadow-none hover:text-foreground"
            >
              Accessibility
            </TabsTrigger>
          </TabsList>
        </div>
        
        <TabsContent value="preview" className="relative mt-6">
          <div className="relative flex min-h-[500px] w-full items-center justify-center overflow-hidden rounded-2xl border border-black/10 dark:border-white/10 bg-white dark:bg-[#111] shadow-sm">
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(0,0,0,0.02)_1px,transparent_1px)] dark:bg-[radial-gradient(circle_at_center,rgba(255,255,255,0.02)_1px,transparent_1px)]" style={{ backgroundSize: '16px 16px' }} />
            <div className="z-10 text-foreground/40 font-medium bg-black/[0.02] px-4 py-2 rounded-lg border border-black/5 dark:border-white/5 shadow-sm">Interactive Python {name} Preview</div>
          </div>
        </TabsContent>
        
        <TabsContent value="python" className="mt-6">
          <div className="rounded-2xl border border-black/10 dark:border-white/10 bg-[#0a0a0a] p-4 shadow-sm relative overflow-hidden">
            <div className="absolute right-4 top-4 text-[10px] uppercase font-mono text-white/30 border border-white/10 px-2 py-0.5 rounded">Python</div>
            <pre className="text-sm font-mono text-white/80 overflow-x-auto p-4 pt-6">
              <code>{`from lifeofpy.components import ${name.replace(" ", "")}

def main():
    component = ${name.replace(" ", "")}(
        text="Click Me", 
        variant="primary"
    )
    component.pack(pady=20, padx=20)

if __name__ == "__main__":
    main()`}</code>
            </pre>
          </div>
        </TabsContent>

        <TabsContent value="react" className="mt-6">
          <div className="rounded-2xl border border-black/10 dark:border-white/10 bg-[#0a0a0a] p-4 shadow-sm relative overflow-hidden">
            <div className="absolute right-4 top-4 text-[10px] uppercase font-mono text-white/30 border border-white/10 px-2 py-0.5 rounded">TSX</div>
            <pre className="text-sm font-mono text-white/80 overflow-x-auto p-4 pt-6">
              <code>{`import { ${name.replace(" ", "")} } from "@/components/ui/${slug}"

export function Example() {
  return (
    <${name.replace(" ", "")} variant="primary">
      Click Me
    </${name.replace(" ", "")}>
  )
}`}</code>
            </pre>
          </div>
        </TabsContent>

        <TabsContent value="a11y" className="mt-6">
          <div className="rounded-2xl border border-black/10 dark:border-white/10 bg-white dark:bg-[#111] p-8 shadow-sm">
             <h3 className="text-lg font-semibold mb-4">Accessibility Notes</h3>
             <ul className="list-disc pl-5 space-y-2 text-foreground/70 text-sm">
               <li>Supports full keyboard navigation using Tab and Shift+Tab.</li>
               <li>Exposes standard WAI-ARIA roles mapped to desktop accessibility APIs (UIAutomation).</li>
               <li>Ensures WCAG AA compliance with a contrast ratio of at least 4.5:1.</li>
               <li>Screen reader announced states (e.g. checked, expanded, disabled) are fully supported out of the box.</li>
             </ul>
          </div>
        </TabsContent>
      </Tabs>

      {/* INSTALLATION */}
      <div className="space-y-6 pt-10">
        <h2 className="text-2xl font-semibold tracking-tight text-foreground border-b border-black/5 dark:border-white/5 pb-4">Installation</h2>
        <div className="relative group">
          <pre className="overflow-x-auto rounded-xl border border-black/10 dark:border-white/10 bg-[#0a0a0a] p-6 text-sm font-mono text-white/80 shadow-inner">
            <code><span className="text-white/30 select-none mr-4">$</span>uvx lifeofpy add {slug}</code>
          </pre>
          <Button
            size="icon"
            variant="ghost"
            className="absolute right-4 top-4 h-8 w-8 text-white/40 hover:text-white hover:bg-white/10 opacity-0 transition-opacity group-hover:opacity-100"
            onClick={handleCopy}
          >
            {copied ? <Check className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
          </Button>
        </div>
      </div>

      {/* API REFERENCE (MOCK) */}
      <div className="space-y-6 pt-10">
        <h2 className="text-2xl font-semibold tracking-tight text-foreground border-b border-black/5 dark:border-white/5 pb-4">API Reference</h2>
        <div className="w-full overflow-x-auto rounded-xl border border-black/10 dark:border-white/10 bg-white dark:bg-[#0a0a0a] shadow-sm">
          <table className="w-full text-left text-sm text-foreground/70">
            <thead className="border-b border-black/10 dark:border-white/10 bg-black/5 dark:bg-white/5 text-foreground/50">
              <tr>
                <th className="px-6 py-4 font-medium">Prop</th>
                <th className="px-6 py-4 font-medium">Type</th>
                <th className="px-6 py-4 font-medium">Default</th>
                <th className="px-6 py-4 font-medium">Description</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-black/5 dark:divide-white/5">
              <tr className="hover:bg-black/5 dark:hover:bg-white/5 transition-colors">
                <td className="px-6 py-4 font-mono text-foreground">variant</td>
                <td className="px-6 py-4 font-mono text-foreground/50">Literal["primary", "secondary", "ghost"]</td>
                <td className="px-6 py-4 font-mono text-foreground/40">"primary"</td>
                <td className="px-6 py-4">The visual style variant of the component.</td>
              </tr>
              <tr className="hover:bg-black/5 dark:hover:bg-white/5 transition-colors">
                <td className="px-6 py-4 font-mono text-foreground">size</td>
                <td className="px-6 py-4 font-mono text-foreground/50">Literal["sm", "md", "lg"]</td>
                <td className="px-6 py-4 font-mono text-foreground/40">"md"</td>
                <td className="px-6 py-4">The size of the component.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}
