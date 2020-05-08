describe('Smoke Tests', () => {
  it('Loads the index', () => {
    cy.visit('/')
  })
  it('Loads the submissions form', () => {
    cy.visit('/new')
  })
})
