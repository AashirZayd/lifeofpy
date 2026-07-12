import * as React from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"

export default function StudioPage() {
  return (
    <div className="container max-w-screen-2xl mx-auto py-12 px-4 md:px-8 space-y-10">
      <div className="space-y-4">
        <h1 className="text-4xl font-bold tracking-tight">Studio</h1>
        <p className="text-lg text-muted-foreground max-w-2xl">
          Your creative workspace. Manage your collections, bookmarks, and contributions to the LifeOfPy ecosystem.
        </p>
      </div>

      <Tabs defaultValue="overview" className="space-y-8">
        <TabsList>
          <TabsTrigger value="overview">Overview</TabsTrigger>
          <TabsTrigger value="bookmarks">Bookmarks</TabsTrigger>
          <TabsTrigger value="collections">Collections</TabsTrigger>
          <TabsTrigger value="contributions">Contributions</TabsTrigger>
        </TabsList>
        <TabsContent value="overview" className="space-y-8">
          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
            <Card>
              <CardHeader className="pb-2">
                <CardDescription>Recent Components</CardDescription>
                <CardTitle className="text-2xl">12</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-xs text-muted-foreground">+2 from last week</p>
              </CardContent>
            </Card>
            <Card>
              <CardHeader className="pb-2">
                <CardDescription>Bookmarks</CardDescription>
                <CardTitle className="text-2xl">48</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-xs text-muted-foreground">Saved for later</p>
              </CardContent>
            </Card>
            <Card>
              <CardHeader className="pb-2">
                <CardDescription>Collections</CardDescription>
                <CardTitle className="text-2xl">3</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-xs text-muted-foreground">Personal packs</p>
              </CardContent>
            </Card>
            <Card>
              <CardHeader className="pb-2">
                <CardDescription>Contributions</CardDescription>
                <CardTitle className="text-2xl">1</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-xs text-muted-foreground">Merged PRs</p>
              </CardContent>
            </Card>
          </div>

          <div className="grid gap-6 md:grid-cols-2">
            <Card className="col-span-1">
              <CardHeader>
                <CardTitle>Continue Building</CardTitle>
                <CardDescription>Pick up where you left off</CardDescription>
              </CardHeader>
              <CardContent className="h-[200px] flex items-center justify-center bg-muted/20 m-6 mt-0 rounded-md">
                <span className="text-muted-foreground text-sm">No recent activity</span>
              </CardContent>
            </Card>
            <Card className="col-span-1">
              <CardHeader>
                <CardTitle>Recent Releases</CardTitle>
                <CardDescription>New components added to the registry</CardDescription>
              </CardHeader>
              <CardContent className="space-y-4">
                {['v1.0.0 Command Palette', 'v1.0.0 DataTable', 'v1.0.0 Dialog'].map((release) => (
                  <div key={release} className="flex items-center justify-between border-b pb-4 last:border-0 last:pb-0">
                    <span className="font-medium text-sm">{release}</span>
                    <span className="text-xs text-muted-foreground">2 days ago</span>
                  </div>
                ))}
              </CardContent>
            </Card>
          </div>
        </TabsContent>
      </Tabs>
    </div>
  )
}
