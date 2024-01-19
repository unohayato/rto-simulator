def calc_rto(rtt_lst):
  ret = []
  
  alpha = 0.125
  beta = 0.25
  
  for i in range(1, len(rtt_lst) + 1):
    rtt = rtt_lst[i-1]
    if i == 1:
      ertt = rtt
      dvrtt = rtt
      devrtt = rtt / 2
      rto = ertt + (4 * devrtt)
    else:
      devrtt = (1 - beta) * devrtt + beta * abs(rtt - ertt)
      ertt = (1 - alpha) * ertt + alpha * rtt
      rto = ertt + (4 * devrtt)
    ret.append([i, rtt, ertt, devrtt, rto])
  
  return ret
    