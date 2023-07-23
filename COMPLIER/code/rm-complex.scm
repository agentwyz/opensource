(define-syntax letv*
    (syntax-rules ()
        [(_ )]))



(define remove-complex-opera*
    (lambda (exp)
        (define temp* #f)
        
        (define new-t
            (lambda ()
                (let ([t (unique-name 't)])
                    (set-box! temp* (cons t (unbox temp*)))
                    t)))
        
        (define rm1
            (lambda (exp)
                (set! temp* (box '()))
                (let ([exp* (make-begin (rem `()))]))
        
        ))

        (define rm)

                    
    ))