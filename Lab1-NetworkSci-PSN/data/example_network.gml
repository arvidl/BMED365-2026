graph [
  name "Protein-interactions"
  node [
    id 0
    label "1"
    function "Tumor suppressor"
  ]
  node [
    id 1
    label "2"
    function "Ubiquitin ligase"
  ]
  node [
    id 2
    label "3"
    function "DNA repair"
  ]
  edge [
    source 0
    target 1
    interaction "binding"
    strength 0.9
  ]
  edge [
    source 0
    target 2
    interaction "cooperation"
    strength 0.7
  ]
]
