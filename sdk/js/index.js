export class BridgeTraceSDK {
  constructor(baseUrl, apiKey = null, tenantId = 'public') {
    this.baseUrl = baseUrl.replace(/\/$/, '');
    this.apiKey = apiKey;
    this.tenantId = tenantId;
  }

  _headers() {
    const h = { 'X-Tenant-ID': this.tenantId };
    if (this.apiKey) h['X-API-Key'] = this.apiKey;
    return h;
  }

  async trace(sourceId, maxHops = 5, minAmount = 0) {
    const res = await fetch(`${this.baseUrl}/api/v2/trace`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...this._headers() },
      body: JSON.stringify({ source_id: sourceId, max_hops: maxHops, min_amount: minAmount })
    });
    if (!res.ok) throw new Error(`trace failed: ${res.status}`);
    return await res.json();
  }
}
