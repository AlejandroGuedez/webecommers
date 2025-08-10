import { test, expect } from '@playwright/test'

test('navegación básica', async ({ page }) => {
  await page.goto('/')
  await expect(page.locator('h1')).toContainText('Storefront')
})
