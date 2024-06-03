---
icon: cache
---

# Page Reference

## Database

Image  | Title Judul | Document | Tags
---    | ---         | ---      | ---
Data   | Data        | Data     | Data




==- Screenshot
![](/static/database.png)
===


## Search Code

```js
import wixData from 'wix-data';

// Function to perform search
function performSearch() {
    let searchValue = $w('#searchInput').value;

    // Query the "References" collection
    wixData.query('References')
        .contains('title', searchValue) // Adjust field as needed
        .or(wixData.query('References').contains('description', searchValue))
        .find()
        .then((results) => {
            // Set the data for the repeater
            $w('#repeater').data = results.items;
        });
}

// Set the button click event
$w.onReady(() => {
    $w('#searchButton').onClick(() => {
        performSearch();
    });
});
```