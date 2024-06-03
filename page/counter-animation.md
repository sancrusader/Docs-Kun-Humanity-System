---
icon: hubot
---
# Counter Animation

![](/static/count.png)

!!!
WIX DEV MODE
!!!

## Initial Setup

```js
$w.onReady(function () {
    $w('#text133').text = "0";
    $w('#text168').text = "0";
    $w('#text171').text = "0";
```
- This part sets the initial text values of three elements (#text133, #text168, and #text171) to "0" when the page is ready.

## Viewport Trigger
```js
$w('#Section1List').onViewportEnter(async () => {
    await countElement('#text133', 0, 96000);
    await countElement('#text168', 0, 800);
    await countElement('#text171', 0, 56);
})
```
- This segment adds an event listener to the element #Section1List. When this element enters the viewport (i.e., becomes visible on the screen), it triggers the asynchronous countElement function for three different text elements.

## Count Element Function

```js
function countElement(element, startValue, endValue, prefix = "", suffix = "") {
    const duration = 1000;
    const increment = (endValue - startValue ) / (duration / 20);
    let currentValue = startValue;

    const timer = setInterval(() => {
        currentValue += increment;
        if (currentValue > endValue) {
            currentValue = endValue; // Ensure it does not exceed endValue
        }
        $w(element).text = prefix + `${Math.round(currentValue).toLocaleString('de-DE')}${suffix}`;

        if (currentValue >= endValue) {
            clearInterval(timer);
        }
    }, 20);
}

```

- This function animates the counting of the text elements from a starting value to an end value over a set duration (1000 milliseconds). The count is updated every 20 milliseconds until it reaches the end value.

- `prefix` and `suffix` parameters allow for adding any desired text before or after the number.

- The `Math.round(currentValue).toLocaleString('de-DE')` formats the number according to German formatting rules (e.g., using commas as thousand separators).