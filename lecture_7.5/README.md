### Задание 3
#### Программа 1
```text
package main

import "fmt"

func main() {
    fmt.Print("Enter amount meters: ")
    var meters float64
    fmt.Scanf("%f", &meters)

    foot := meters * 0.3048

    fmt.Println(foot)    
}
```
#### Программа 2
```text
package main

import "fmt"

func main() {
    x := []int{48,96,86,68,57,82,63,70,37,34,83,27,19,97,9,17,}
    min := x[0]
    for i := 1; i < len(x); i++ {
	if min > x[i] {
	  min = x[i]
	}
    } 

    fmt.Println(min)    
}
```
#### Программа 3

```text
package main

import "fmt"

func main() {
    
    for i := 1; i < 100; i++ {
	if i % 3 == 0 {
	  fmt.Println(i) 
	}
    } 

       
}
```
