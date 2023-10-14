const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // Navigate to the e-commerce page
  await page.goto('https://mydawa.com/products/medical-conditions/stomach-care/-digestive-health');

  // Wait for the page to load fully (you may need to adjust this time)
  await page.waitForTimeout(3000);

  // Extract image URLs
  const imageUrls = await page.evaluate(() => {
    const images = Array.from(document.querySelectorAll('img'));
    return images.map(img => img.src);
  });

  // Print the image URLs
  console.log(imageUrls);

  // Close the browser
  await browser.close();
})();
