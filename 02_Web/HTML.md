# HTML_01 | 20190729

## 1. WEB SERVICE

* Client (클라이언트) <-> Server (서버)
* Client requests service. Server responses to the client's request.
* Browser을 통해서 요청을 보낸다
* 요청의 종류
  * get (받다) ex) post 외 전부. 대다수를 차지함.
  * post(보내다)  ex) 로그인, 회원가입 정보 입력 등
* 서버의 핵심: 요청을 받고 분석해서, 일을 해서 클라이언트에게 답장을 주는 것
* 결국, client의 요청은 user가 뒤에서 보내게 되고, server의 응답은 program이 조정하게 됨



## 2. Web

* Dynamic Web
* Web Application program (Web APP)



## 3. URL

URL = Uniform Resource Locator/ 파일 식별자

네트워크 상에서 자원이 어디 있는지 알려주기 위한 고유 규약

URL은 웹사이트 주소 뿐만 아니라, 컴퓨터 네트워크 상의 자원을 모두 나타낼 수 있다





## 4. HTML

* HTML: Hyper Text Markup Layout

* HTML is used to create the structure and content of a webpage.

* Most HTML elements contain opening and closing tags with raw test or other HTML tags between them.

  ```html
  # element
  <p>Hello World!</p>
  #opening tag - content - closing tag
  ```

  

* HTML elements can have "nest" relationship among them.

  * When one element is nested inside of another element, nested element is considered as the child element and another element is considered as the parent element.

  

### 4.1 Main Elements and Tags

- DOM Tree: 태그는 중첩되어 사용가능하며, 이때 다음과 같은 관계를 같는다. 안에 있는 태그는 밖에 있는 태그의 자식이다. 부모-자식 관계가 있으며, 더 큰 관계로는 안에 있는 태그들의 밖에 있는 태그의 후손들이라고 한다. 같은 위치에 있는 태그들은 형제 관계이다.

- Document type declaration: `<!DOCTYPE html>`

  - HTML must start with document type declaration; `<!DOCTYPE html>`
  - This declaration is an instruction for the browser telling what type of document to expect.
  
- HTML: `<html>-</html>`

  - creating HTML structure and content
  - opening tag after declaring document type and closing tag at the last line of document
  
- head: `<head>-</head>`

  - The head element contains the metadata for a web page. Metadata is information about the page that isn't displayed directly on the web page.
  
- body: `<body> - </body>`

  - Any visible content should be placed within the body tags.
  
- header: `<header>-</header>`
  - represents introductory content of its nearest parent sectioning content or root element
  - If its nearest parent section is the body element, then it applies to the whole page.
  - contains a group of introductory or navigational aids

-  heading: `<h1> - </h1>` 

  - heading tags are used to enlarge text.
  - it has size variety from h1 to h6.
  - `<h1>` is always used for main headings.

- title: `<title>-</title>`

  - `title` tags contain the title of the web page. The title spcified in the title tag is displayed in a browser's tab.

- paragraph: `<p> - </p>`

  - Paragraphs contain a block of plain text.
  - the p element is usually nested inside the body  or div element.

- division: `<div>-</div>`

  - The div element is a container that divides the page into sections.
  - It is used for better readability.
  - One group of elements such as heading and paragraph is inside the opening and closing tag of div.
  - div element is the child of body element.

- span: `<span>-</span>`

  - span contains short pieces of text of other HTML.
  - used to separate small pieces of content from other content that are on the same line
  - It is used for styling content for such as id, class.

- break: `<br>`

  - used for line breaking; it makes line space between contents.
  - only composed of a starting tag

- Styling text elem

  - `<em>-</em>` : emphasizes text by *italic* emphasis
  - `<strong>-</strong>` : highlights important text by **bold** emphasis

- Lists

  - Unordered List: `<ul>-</ul>`
    - creating a list of items in no particular order with a bullet point
    - Individual list items must be added to a list using the `<li>-</li>` tag.
  - Ordered List:  `<ol>-</ol>`
    - creating a list of items in particular order with numbers
    - Individual list items must be added to a list using the `<li>-</li>` tag.

- Image: `<img src="URL" alt="name"/>`

  - add an image to a web page
  - a self-closing tag
  - `src` (source) is an attribute that is used for setting to the image's source. The value of src must be the uniform resource locator (URL) of the image.
  - `alt` (alternative text) is an attribute that is used for bringing meaning to the images. The value of alt should be a description of the image. When images cannot be loaded or seen, alt value is presented as the image's description.

- Videos: `<video src="URL" width="number" height="number" controls> - </video>`

  - Displaying videos
  - Similar to img tag, it must contain the source of video in `src` tag. `width` and `height` tag is the size of video player. 
  - `controls` attribute instructs the broswer to include basic video controls: pause, play and skip.
  - The text between the opening and closing video tags wiill only be displayed if the browser is unable to load the video.

- Linking: `<a href="URL" target="_blank"> - </a>`

  - Adding links to a web page

  - `<a>` is an anchor element including the text of the link in between the opening and closing tags.

  - `href` (hyperlink reference) attribute must be used in an `a` element to link to an address of a file or website.

  - `target="_blank"` attribute is used to open a new page of browser when want users to return to original website.

  - When linked web pages are ought to be an internal page, `href` tag should contain internal page's address which should be in a form of "./docu_name.html". Internal pages must be in the same folder.

  - Between the opening and closing tag of `a`, contents can be image or text. When you want to use image as link, `img` tag should be in between `a` element.

  - When the target of links are on the same page, the target must have an `id` to assign link. The target link a string containing the `#` character and the target element's `id`. 

    - ex) `<a href="#top">Top</a>`

      

### 4.2 Attributes

- Attributes are content added to the opening tag of an element.
- Can be used in several different ways, from providing infromation to changing styling.
- Attributes are made up of the following two parts:
  - The name of the attribute
  - The value of the attribute
- `id` : to specify different content such as <div>s when use more than one element
- When you have to enter several values to one attribute, you use space to identify each value.

### 4.3 Semantic tags

- Semantic tag: Semantic tags are for representing the meaning of contents. It is different from non-semantic tags; semantic tags are used for explaining the usage of contents or the role of contetns in website, html file. Non-semantic tags are div, span, etc. 
- These are new semantic tags in HTML5.
  - `<header></header>` :  header of whole html or section
  - `<nav></nav>` : navigation of whole html
  - `<aside></aside>`: It represents the side space of whole html. It can be used for contents that are less relative to main contents.
  - `<section></section>`: section tags are mostly used for defining each group of contents. It mostly has h1-h6 tags.
  - `<article></article>`:  article tags are used for defining the independent space in html, which contains one news article or forum.
  - `<footer></footer>` : footer of whole html



### 4.4 Tables

- Main element: `<table></table>`

  - The table element will contain all of the tabular data planned to be on display.

- Table Body: `<tbody></tbody>`

  - When a table grows to contain a lot of data and vecome very long, the table can be sectioned off so that it is easier to manage. Long tables cna be sectioned off using the table body element. 

  - The tbody element should contain all of the table's data, excluding table headings.

    ```html
    <table>
    	<thead>
    		<tr>
    			<th> Name <th>
    			<th> Age <th>
    			<th> Role <th>
    		</tr>
    	</thead>
    	<tbody>
    		<tr>
    			<td>Moon</td>
    			<td>20</td>
    			<td>Leader</td>
    		</tr>
    		<tr>
    			<td>Kim</td>
    			<td>22</td>
    			<td>Manager</td>
    		</tr>
    	</tbody>
        <tfoot>
        	<th>Total</th>
            <td>2</td>
        </tfoot>
    </table>
    
    ```

- Table must contain the rows, columns, and cells that willl hold data.

  - rows: `<tr></tr>`

  - table data: `<td></td>`

    ```html
    <tr>
    	<td>first cell</td>
    	<td>second cell</td>
    </tr>
    ```

- Table heading: Titles of table data to describe what the data represents. Table heading must be placed within a table row.

  ```html
  <thead>  
        <tr>
          <th>Company Name</th>
          <th>Number of Items to Ship</th>
          <th>Next Action</th>
        </tr>
  </thead> 
  ```

- Table footer: `<tfoot></tfoot>`

  - The bottom part of a long table can be sectioned off using the tfoot element. Footers are often used to contain sums, differences and other data results.

    ```html
    <tfoot>
    	<th>Total</th>
        <td>$22M</td>
        <td>$12.5M</td>
    </tfoot>
    ```

    

- Table borders: Table borders set a line around table to present table clearly. It can be made with the border attribute, but it is usually defined in CSS.

- Spanning Columns & Rows:

  - `colspan`: data can span columns (using multiple columns) using the colspan attribute. 

  ```html
  <tr>
  	<td>first col</td>
  	<td>second col</td>
  	<td>third col</td>		
  </tr>
  <tr>
  	<td colspan="2"> first & second col using</td>
  	<td> third col </td>
  </tr>
  ```

  - `rowspan`: data cna span rows (using multiple rows) using the rowsapn attribute.

  ```html
  <tr>
    	<td>Davie's Burgers</td>
    	<td rowspan="2">2</td>
    	<td>Send Invoice</td>
  </tr>
  <tr>
    	<td>Baker's Bike Shop</td>
    	<td>Send Invoice</td>
  </tr>
  ```



### 4.5 Forms

- HTML form element is for collecting information to send somewhere else. It provides a space for users to type in or to provide an input.

- It is essential for sending and receiving information as a network of computers. Computers need an HTTP requests to know how to communicate.

- It must contain the `action` attribute which determines where the information is send and the `method` attribute that determines a HTTP verb included in the HTTP request.

  ```html
  <form action="/exmaple.html" method="POST">
      <input type="#" name= "#">
  </form>
  ```

- The form element can also contain child elements. It is healpful to expalain what a form is for.

- The `input` element has a `type` attribute which determines how it reders on the web and what kind of data it can accpet.

- The `input` element also has a `name`attribute which send information in the input when the form is submitted.

- The `label` element is used for explaining what the input is used for.

- The label element has an opening and closing tag and displays text that is written between the opening and closing tags. It has `for` attribute which reference the value of the `id` attribute of `input`.

- To associate a label and an input, the input needs an `id` attribute.

  ```html
  <form action="/example.html" method="POST">
      <label for="meal">What do you want to eat?</label>
      <br>
      <input type="text" name="food" id="meal">    
  </form>
  ```

  ![rendered form with labeled text field](https://s3.amazonaws.com/codecademy-content/courses/learn-html-forms/label+-+text+input.png)

#### 4.5.1. Types of input

- Text input: redering a text field that users can type "text" into

  - `minlength` and `maxlength` attribute can set the minimum and maximum length of text input.
  - `pattern` attribute can set the specific guidelines for users to type in. 

- Password input: redering an input for sensitive information. replacing input text with another character like * or dot.

- Number input: Restricting what users type into the input field to just numbers. With `step` attribute, can create arrows inside the input field to increase or decrease by the value of the `step` attribute.

- Range input: Limiting what numbers users could type by creating a slider. Must have `min` and `max` attribute to set the minimum and maxmumm values of the slider.

- Checkbox input: Presenting mutiple options to users and allow them to select any number of options. It must have `value` attribute to identify each checkbox.

  - Each input has the same value for the name.

  - Each input has a unique id to pair with a label.

    ```html
    <input id="lettuce" name="topping" type="checkbox" value="lettuce">
    <label for="lettuce">Lettuce</label>
             
    <input id="tomato" name="topping" type="checkbox" value="tomato">
    <label for="tomato">Tomato</label>
              
    <input id="cheese" name="topping" type="checkbox" value="cheese">
    <label for="cheese">Chesse</label>
    ```

- Radio Button input: Presenting mutiple options to suers and allow them to choose only one selection.

  ```html
  <form>
      <p>What is sum of 1 + 1?</p>
      <input type="radio" id="two" name="answer" value="2">
      <label for="two">2</label>
      <br>
      <input type="radio" id="eleven" name="answer" value="11">
      <label for="eleven">11</label>
  </form>
  ```

  ![rendered form containing radio buttons](https://s3.amazonaws.com/codecademy-content/courses/learn-html-forms/radioInput+-+labeled.png)

- Select Box / Dropdown list:  Representing an organized list and allowing users to choose one option form the list.

  ```html
  <form>
  	<label for="bun">What type of bun would you like?</label>
          <select id="bun" name="bun">
              <option value="sesame">Sesame</option>
              <option value="potato">Potato</option>
              <option value="mushroom">Mushroom</option>
          </section>
  </form>
  ```

  ![rendered dropdown list with the all options showing](https://s3.amazonaws.com/codecademy-content/courses/learn-html-forms/dropdown+list+-+revealed.png)

- Datalist input: Creating text field that users can type into and filter options from the `datalist`. Input has `list` attribute to associate to the `id` of the `datalist` . It is different from `select` that users can type in the input field to search for a particular option and if none of the options match, user can still use what they typed in.

  ```html
  <form>
      <label for="city">Ideal city to visit?</label>
      <input type="text" list="cities" id="city" name="city">
      
      <datalist id= cities>
          <option value="Seoul"></option>
          <option value="Barcelona"></option>
          <option value="Amsterdam"></option>
          <option value="Manila"></option>
  </form>
  ```

  ![clicking on the input field reveals a dropdown  list](https://s3.amazonaws.com/codecademy-content/courses/learn-html-forms/datalist+-+revealed.png)

- Textarea element

  - When users need to write more information, like a blog post, `textarea` element can be used.

  - It is used to create a bigger text field for users to wrtie more text. 

  - It can have attributes `rows` and `cols` to determine the amount of rows and columns for the textarea.

    ```html
    <form>
        <label for="blog">New Blog Post:</label>
        <br>
        <textarea id="blog" name="blog" rows="5" cols="30">	</textarea>
    </form>
    ```

    ![rendered empty textarea element](https://s3.amazonaws.com/codecademy-content/courses/learn-html-forms/textarea+-+blank.png)

- Submit Form: Making a submit button in a `form` 

  ```html
  <input type="submit" value= "send">
  ```



#### 4.5.2 Forms Validation

(1) Server-side Validation

- Data is sent to another machine (typically a server) for validation.
- example: login page checks username and password 

(2) Client-side Validation

- Checking the data on the client's browser

- Validation occurs before data is sent to the server.



- If validations on a `form` do not pass, the user gets a message explaining why and the form cannot be submitted.
- Validations help ensure that input data is correct and safe for servers.
- Validations help give users immediate feedback on what they need to fix.