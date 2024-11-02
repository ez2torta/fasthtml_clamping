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

