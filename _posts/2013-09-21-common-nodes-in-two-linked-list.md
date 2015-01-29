---
layout: post
title: "找两个链表的公共节点"
category: Past
description: 编程之美 3.6
---
首先考虑两个链表无环的情况。

将链表a的尾节点指向头节点从而形成环。用快慢指针遍历链表b，一个一次移动2单位，另一个移动1单位。如果不相遇则不存在公共节点。如果相遇，则让其中一个指针指向b，两个指针以1单位/次的速度移动，直到相遇。相遇时指向的节点就是公共节点的起始。最后记得将a的尾节点恢复。代码如下。

其次考虑有环的情况。用快慢指针探测a中是否有环。如果有则，将使p指向a的尾节点，p的next指向null。按照上面的方法遍历b。如果遍历的过程中遇到p，则将p指向a继续遍历。如果未遇到p或者无环，则不存在公共节点。最后仍然将a的尾节点恢复。

```java
static class LinkedList {
	LinkedList next;
	public LinkedList(LinkedList next) {
		this.next = next;
	}
}

static LinkedList calc(LinkedList a, LinkedList b) {
	// set tail point to a
	LinkedList p = a;
	while (p.next != null) {
		p = p.next;
	}
	p.next = a;

	if (b == null || b.next == null)
		return null;
	LinkedList fast = b.next.next, slow = b.next;
	while (fast != null && fast.next != null && fast != slow) {
		fast = fast.next.next;
		slow = slow.next;
	}
	if (fast != slow) {
		return p.next = null;
	} else {
		slow = b;
		while (fast != slow) {
			fast = fast.next;
			slow = slow.next;
		}
		p.next = null;
		return slow;
	}
}

public static void main(String[] args) {
	LinkedList common = new LinkedList(new LinkedList(new LinkedList(null)));
	LinkedList a = new LinkedList(new LinkedList(common));
	LinkedList b = new LinkedList(new LinkedList(new LinkedList(
			new LinkedList(common))));
	LinkedList r = calc(a, b);
	System.out.println(r == common);

}
```