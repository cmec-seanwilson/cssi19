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

// Task 1
const dogName1 = "Steve";
const dogType1 = "beagle";

// Complete Task 1 Below

console.log(`I will walk ${dogName1} today at 12:00pm`)

const dogName2 = "Joe";
const dogType2 = "bulldog";

// Complete Task 2 Below

console.log(`I will walk ${dogName2} today at ${dogType2 === 'corgi' ? '12:00' : '1:00'}pm`)

const dogName3 = "Lola";
const dogType3 = "poodle";

// Complete Task 3 Below

if (dogType3 === 'beagle' || dogType3 === 'corgi') {
    console.log(`I will walk ${dogName3} today at 12:00pm`)
} else if (dogType3 === 'bulldog') {
    console.log(`I will walk ${dogName3} today at 1:00pm`)
} else { 
    console.log(`I will walm ${dogName3} today at 2:00pm`)
}
     
// Extension

let dogOwner = 'sean'
let extDogName = 'Spike'
let normalizedDogName = extDogName.toLowerCase()
let extDogType = 'beagle'
let allowedDogNames = [
    'spike',
    'jeremy',
    'lola',
    'peaches',
    'steve'
]
let time;

switch (extDogType) {
    case extDogType === 'corgi' || extDogType === 'beagle':
        time = '12:00'
        break;
    case extDogType === 'bulldog':
    default:
        time = '1:00'
        break;
}


if (allowedDogNames.includes(normalizedDogName)) {
    console.log(`I, ${dogOwner}, will walk ${extDogName}, one of my favorite dogs, today at ${time}pm`)
}
