import { z } from 'zod'

export const envSchema = z.object({
  NEXT_PUBLIC_API_URL: z.string().url()
})

export type Env = z.infer<typeof envSchema>

export const DEFAULT_CURRENCY = 'ARS'
export const DEFAULT_LOCALE = 'es-AR'
