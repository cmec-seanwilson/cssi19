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

console.log("script is running...");

console.log = function (message) {
    document.write(message + '<br>')
}

function myAlarm (time) {
    console.log(`Hey, Sean, wake up! It's ${time}`)
}

function momAlarm (time) {
    console.log(`Hey, Mom, wake up! It's ${time}`)
}

function familyAlarm (person, time) {
    console.log(`Hey, ${person}, wake up! It's ${time}`)
}

function importantAlarm (message) {
    console.log(message.toUpperCase())
}

// Takes integer time and adds one time, acting a snooze
function snoozeAlarm (time) {
    console.log(`The alarm for ${time} has been changed to ${time + 1}`)
}

function wakeUpEach (people) {
    for (let i = 0; i < people; i++) console.log('Wake up!')
}

myAlarm('7:00 AM')
momAlarm('7:30 AM')
familyAlarm('Dad', '6:00 AM')
familyAlarm('Bro', '10:00 PM')
importantAlarm('If you\'re late one more time, you\'ll be fired!')
snoozeAlarm(3)
wakeUpEach(21)