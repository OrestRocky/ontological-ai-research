// entity_graph.go
// Basic representation of ontological entities in Go

package main

import "fmt"

type Entity struct {
	Name   string
	Parent *Entity
}

func (e *Entity) IsA(target string) bool {
	if e.Name == target {
		return true
	}
	if e.Parent != nil {
		return e.Parent.IsA(target)
	}
	return false
}

func main() {
	being := Entity{"Being", nil}
	mind := Entity{"Mind", &being}
	fmt.Println(mind.IsA("Being")) // true
}
