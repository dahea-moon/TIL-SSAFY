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

* HTML: Hyper Text Transfer Protool

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
- 