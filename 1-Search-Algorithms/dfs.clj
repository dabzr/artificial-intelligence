; Depth-First-Search Algorithm

(defn dfs [graph node path]
  (let [new-path (conj path node) neighbors (get graph node)]
    (cond
      (= node :G) new-path
      (empty? neighbors) nil
      :else
      (some #(dfs graph % new-path) neighbors))))

(def problem {:S [:A :B] :A [:B] :B [:G :A] :G []})

(println (dfs problem :S [])) 


