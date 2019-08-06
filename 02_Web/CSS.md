# CSS | 20190806

## 1.  What is CSS?

- CSS (Cascading Style Sheets) is a language that used to style the HTML content on a web page.

- Ways to write CSS code

  - Inline Styles: code only a line

    ```html
    <p style="color: red; font-family: Arial;">
         I'm learning to code!
    </p>
    ```

  - The <style> Tag: code multiple lines that are same elements

    ```html
    <head>
        <style>
            p {
                color: red;
                font-size: 20px;
            }
        </style>
    </head>
    ```

  - The .css file: craeting a CSS file by using the .css file name extension

    ```html
    <link href="path to the CSS file" type="text/css" rel="stylesheet">
    ```

## 2. SELECTORS

### 1) Tag Name

- select HTML elements by using an element's tag name

- ```css
  p {
  
  }
  h1 {
  
  }
  ```

### 2) Class Name

- Select HTML elements by using an class attribute (must put '.' before class name)

- ```css
  .class_name {
  
  }
  .another_class_name {
  
  }
  ```

- Adding several class name

  - possible to add more than one class name to an HTML element's class attribute

  - ```html
    <h1 class="green bold"> </h1>
    ```

  - **Classes are meant to be reused over many elements.** 

  - can recognize each class by separating them with a space

### 3) ID Name

- Select HTML elements by using their id attribute (must put "#" before id name)

- **ID is meant to style only one element.**

- ```css
  #large-title {
  
  }
  ```

### 4) Specificity & Overriding

- Specificity is the order by which the browser decides which CSS styles will be displayed. Using the lowest degree of specificity at the first, it would be easy to override.
- IDs are the most specific selector in CSS. The only way to override an ID is to add another ID with additional styling.
- Class is more specific than the tag selector.
- Should be in order of tag, class, ID
- Adding more than one tag, class, or ID to a CSS selector increases the specificity of the CSS selector

### 5) Chaining Selectors

- Possible to require an HTML element to have two or more selectors

- ```css
  h1.special {
  
  }
  ```

- The code above would select only the h1 elements that have a class of special.

### 6) Selecting Nested Elements

- Possible to select elements that are nested within other HTML elements

- ```html
  <ul class="main-list">
      <li>...</li>
      <li>...</li>
      <li>...</li>
  </ul>
  ```

- ```css
  .main-list li {
  
  }
  ```

- The code above would select `.main-list` element and li elements that are nested in `.main-list` element.

### 7) Important

- `!important` is even more specific than IDs.
- `!important` is placed behind style attribute.
- It will override any style no matter how specific it is.
- It is not recommended to use; except in a very specific case.

### 8) Multiple Selectors

- Add CSS styles to multiple CSS selectors all at once

- ```css
  h1,
  .menu {
  	font-family: Georgia;
  }
  ```

  

