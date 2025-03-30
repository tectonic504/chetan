import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

/**
 * Shared layout configurations
 *
 * you can customise layouts individually from:
 * Home Layout: app/(home)/layout.tsx
 * Docs Layout: app/docs/layout.tsx
 */
export const baseOptions: BaseLayoutProps = {
  nav: {
    title: (
      <>
        <svg
          id="Layer_1"
          data-name="Layer 1"
          viewBox="0 0 300 300"
          version="1.1"
          xmlns="http://www.w3.org/2000/svg"
          height={24}
          width={24}
        >
          <path
            d="M446.67,225a75,75,0,0,1-75-75,75,75,0,1,1-150,0,75,75,0,0,1-75,75,75,75,0,0,1,0,150,75,75,0,0,1,75,75,75,75,0,0,1,150,0,75,75,0,0,1,75-75,75,75,0,0,1,0-150Z"
            transform="translate(-146.67 -150)"
            style={{fill: "currentcolor"}}
          />
        </svg>
        Chetan
      </>
    ), 
  },
};
