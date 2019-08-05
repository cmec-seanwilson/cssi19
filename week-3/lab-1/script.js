// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

let currentPad = 0;

const frogger = document.querySelector('#frog')
const positions = [
  {
    top: 50,
    left: 17
  },
  {
    top: 23,
    left: 33.5 
  },
  {
    top: 50,
    left: 50.5
  },
  {
    top: 75,
    left: 67
  },
  {
    top: 50,
    left: 82
  }
]


function advanceFrog (e) {
  if (currentPad <= positions.length - 1) {
    const position = positions[currentPad]
    document.querySelector('.active').classList.remove('active')
    document.querySelector('#lilypad' + (currentPad + 1)).classList.add('active')
    currentPad++
    frogger.style.left = position.left + '%'
    frogger.style.top = position.top + '%'
  } else {
    currentPad = 0
  }
  
  // const rect = e.getBoundingClientRect()
}

frogger.addEventListener('click', (e) => {
  advanceFrog(e)
});
