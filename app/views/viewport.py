from fasthtml.common import *

css = Style(
    """
* {
    box-sizing: border-box;
    font-family: Inconsolata, sans-serif;
  }
  .title {
    background-color: #20B2AA;
    color: #FFFFE0;
    font-size: 40px;
    width: calc(100vw - 24px);
    height: fit-content(10vh);
    text-align: center;
    padding: 12px;
    margin: 0;
  }
  .container {
    background-color: #e0d4fc;
    height: 88vh;
    width: calc(100vw - 24px);
    padding: 12px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .rect {
    background-color: #2c35e8;
    color:  #FFFFE0;
    width: clamp(250px, 50vw, 600px);
    height: 150px;
    font-weight: normal;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 20px;
  }
  
  .width {
    font-size: 30px;
  }
  
  .clamp {
    font-size: 30px;
    color: #2c35e8;
  }
  
  .viewport-container {
    padding: 6px 12px;
    font-size: 20px;
  }
  
  .viewport {
    color: #004f5e;
    font-size: 30px;
  }
  
  .resize {
    font-size: 20px;
  }
  
"""
)

js = Script(
    """
const rect = document.querySelector('.rect')
const text = document.querySelector('.width')
const viewport = document.querySelector('.viewport')
const rectStyle = window.getComputedStyle(rect)
const state = {
  calculate() {
    this.width = parseInt(rectStyle.width).toFixed(0)
    text.textContent = `width: ${this.width}px`
    this.viewport = window.innerWidth
    viewport.textContent = `viewport: ${this.viewport}px`
  },
  width: '',
  viewport: ''
}

state.calculate()

window.addEventListener('resize', function(){
  state.calculate()
});


"""
)

def Test():
    resize_p = P("Resize the viewport and watch the width change", cls="resize")
    viewport = P(cls="viewport")
    viewport_container = Div(viewport, cls="viewport-container")
    width = P(cls="width")
    rect = Div(width, cls="rect")
    clamp = P("width: clamp(250px, 50vw, 600px);", cls="clamp")
    main = Main(
        Div(resize_p, viewport_container, rect, clamp, cls="container"),
        hx_ext="ws",
        ws_connect="/gol",
    )
    footer = Footer(
        P(
            "Tortita (dot) net 2024",
            AX("Github", href="https://github.com/ez2torta", target="_blank"),
        )
    )
    return H1("Clamp () Example", cls="title"), main, footer, js