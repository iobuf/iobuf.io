(define (filter predicate sequence)
  (cond ((null? sequence) nil)
	((predicate (car sequence))
	 (cons (car sequence)
	       (filter predicate (cdr sequence))))
	(else (filter predicate (cdr sequence)))))

(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
    (op (car sequence)
	(accumulate op initial (cdr sequence)))))

; tree
(define (enumerate-tree tree)
  (cond ((null? tree) nil)
	((not (pair? tree)) (list tree))
	(else (append (enumerate-tree (car tree))
		      (enumerate-tree (cdr tree))))))
(define (sum-odd-squares tree)
  (accumulate +
	      0
	      (map squares
		   (filter odd? (enumerate-tree tree)))))

; fibonacci
(define (enumerate-interval low high)
  (if (> low high)
      nil
    (cons low (enumerate-interval (+ low 1) high))))
(define (even-fibs n)
  (accumulate cons
	      nil
	      (filter even?
		      (map fib (enumerate-interval 0 n)))))