<h2><a href="https://leetcode.com/problems/median-of-two-sorted-arrays/">4. Median of Two Sorted Arrays</a></h2><h3>Hard</h3><hr><div element-id="998"><p element-id="997">Given two sorted arrays <code element-id="996">nums1</code> and <code element-id="995">nums2</code> of size <code element-id="994">m</code> and <code element-id="993">n</code> respectively, return <strong element-id="992">the median</strong> of the two sorted arrays.</p>

<p element-id="991">The overall run time complexity should be <code element-id="990">O(log (m+n))</code>.</p>

<p element-id="989">&nbsp;</p>
<p element-id="988"><strong class="example" element-id="987">Example 1:</strong></p>

<pre element-id="986"><strong element-id="985">Input:</strong> nums1 = [1,3], nums2 = [2]
<strong element-id="984">Output:</strong> 2.00000
<strong element-id="983">Explanation:</strong> merged array = [1,2,3] and median is 2.
</pre>

<p element-id="982"><strong class="example" element-id="981">Example 2:</strong></p>

<pre element-id="980"><strong element-id="979">Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong element-id="978">Output:</strong> 2.50000
<strong element-id="977">Explanation:</strong> merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
</pre>

<p element-id="976">&nbsp;</p>
<p element-id="975"><strong element-id="974">Constraints:</strong></p>

<ul element-id="973">
	<li element-id="972"><code element-id="971">nums1.length == m</code></li>
	<li element-id="970"><code element-id="969">nums2.length == n</code></li>
	<li element-id="968"><code element-id="967">0 &lt;= m &lt;= 1000</code></li>
	<li element-id="966"><code element-id="965">0 &lt;= n &lt;= 1000</code></li>
	<li element-id="964"><code element-id="963">1 &lt;= m + n &lt;= 2000</code></li>
	<li element-id="962"><code element-id="961">-10<sup element-id="960">6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup element-id="959">6</sup></code></li>
</ul>
</div>