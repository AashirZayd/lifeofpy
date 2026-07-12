"use client"

import * as React from "react"
import { useRouter } from "next/navigation"
import {
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
  CommandSeparator,
} from "@/components/ui/command"
import { Laptop, FileText, Paintbrush, Box, Layers, Code, Play } from "lucide-react"

export function CommandPalette() {
  const [open, setOpen] = React.useState(false)
  const router = useRouter()

  React.useEffect(() => {
    const down = (e: KeyboardEvent) => {
      if (e.key === "k" && (e.metaKey || e.ctrlKey)) {
        e.preventDefault()
        setOpen((open) => !open)
      }
    }

    document.addEventListener("keydown", down)
    return () => document.removeEventListener("keydown", down)
  }, [])

  const runCommand = React.useCallback((command: () => unknown) => {
    setOpen(false)
    command()
  }, [])

  return (
    <CommandDialog open={open} onOpenChange={setOpen}>
      <CommandInput placeholder="Search commands, components, and docs..." className="h-14 px-4 text-base" />
      <CommandList className="pb-4">
        <CommandEmpty>No results found.</CommandEmpty>
        <CommandGroup heading="Quick Links" className="px-2">
          <CommandItem
            onSelect={() => runCommand(() => router.push("/components"))}
            className="rounded-lg py-3 px-4 aria-selected:bg-white/10 aria-selected:text-white"
          >
            <Box className="mr-3 h-5 w-5 text-white/50" />
            <span className="text-base font-medium">Browse Components</span>
          </CommandItem>
          <CommandItem
            onSelect={() => runCommand(() => router.push("/examples"))}
            className="rounded-lg py-3 px-4 aria-selected:bg-white/10 aria-selected:text-white"
          >
            <Play className="mr-3 h-5 w-5 text-white/50" />
            <span className="text-base font-medium">View Examples</span>
          </CommandItem>
          <CommandItem
            onSelect={() => runCommand(() => router.push("/inspiration"))}
            className="rounded-lg py-3 px-4 aria-selected:bg-white/10 aria-selected:text-white"
          >
            <Paintbrush className="mr-3 h-5 w-5 text-white/50" />
            <span className="text-base font-medium">Get Inspired</span>
          </CommandItem>
          <CommandItem
            onSelect={() => runCommand(() => router.push("/docs"))}
            className="rounded-lg py-3 px-4 aria-selected:bg-white/10 aria-selected:text-white"
          >
            <FileText className="mr-3 h-5 w-5 text-white/50" />
            <span className="text-base font-medium">Read Documentation</span>
          </CommandItem>
          <CommandItem
            onSelect={() => runCommand(() => router.push("/studio"))}
            className="rounded-lg py-3 px-4 aria-selected:bg-white/10 aria-selected:text-white"
          >
            <Laptop className="mr-3 h-5 w-5 text-white/50" />
            <span className="text-base font-medium">Open Studio</span>
          </CommandItem>
        </CommandGroup>
        <CommandSeparator className="my-2 bg-white/10" />
        <CommandGroup heading="Components" className="px-2">
          <CommandItem 
            onSelect={() => runCommand(() => router.push("/components/button"))}
            className="rounded-lg py-3 px-4 aria-selected:bg-white/10 aria-selected:text-white"
          >
            <Layers className="mr-3 h-5 w-5 text-white/50" />
            <span className="text-base font-medium">Button</span>
          </CommandItem>
          <CommandItem 
            onSelect={() => runCommand(() => router.push("/components/input"))}
            className="rounded-lg py-3 px-4 aria-selected:bg-white/10 aria-selected:text-white"
          >
            <Code className="mr-3 h-5 w-5 text-white/50" />
            <span className="text-base font-medium">Input</span>
          </CommandItem>
        </CommandGroup>
      </CommandList>
      <div className="flex items-center justify-between border-t border-white/10 bg-black/40 px-4 py-3">
        <div className="flex items-center space-x-2 text-xs text-white/50">
          <span className="font-semibold text-white/80">Tip:</span> Use arrow keys to navigate.
        </div>
        <div className="flex items-center space-x-2 text-xs text-white/40">
          <kbd className="rounded border border-white/20 bg-white/10 px-1.5 py-0.5 font-sans">esc</kbd> to close
        </div>
      </div>
    </CommandDialog>
  )
}
