/// <reference types="vite/client" />

declare global {
    interface ImportMetaEnv {
        readonly VITE_BACKEND_HOSTNAME: string;
        readonly VITE_BACKEND_PORT: string;
        readonly VITE_BACKEND_URL: string;
    }

    interface ImportMeta {
        readonly env: ImportMetaEnv;
    }
}

export {} // Ensures this file is treated as a module
