import { cn } from 'fumadocs-ui/components/api';
import './global.css';
import { DM_Mono, Inter } from 'next/font/google';
import type { ReactNode } from 'react';
import { RootProvider } from 'fumadocs-ui/provider';

const inter = Inter({
  subsets: ['latin'],
});

const codeFont = DM_Mono({
  subsets: ["latin"],
  variable: "--default-mono-font-family",
  display: "swap",
  weight: "400",
});

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <html
      lang="en"
      className={cn(inter.className, codeFont.variable)}
      suppressHydrationWarning
    >
      <body className="flex flex-col min-h-screen">
        <RootProvider
          search={{
            enabled: true,
            options: {
              defaultTag: "examples",
              tags: [
                {
                  name: "Framework",
                  value: "framework",
                },
                {
                  name: "Examples",
                  value: "examples",
                },
              ],
            },
            
          }}
        >
          {children}
        </RootProvider>
      </body>
    </html>
  );
}
