import type { APIRoute } from 'astro';

export const prerender = false;

export const POST: APIRoute = async ({ request }) => {
  const makeWebhookUrl =
    import.meta.env.MAKE_WEBHOOK_URL ||
    (typeof process !== 'undefined' ? process.env.MAKE_WEBHOOK_URL : '');

  if (!makeWebhookUrl) {
    console.error('[submit] MAKE_WEBHOOK_URL is not configured');
    return new Response(JSON.stringify({ ok: false, error: 'server_config' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return new Response(JSON.stringify({ ok: false, error: 'invalid_json' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  try {
    const makeRes = await fetch(makeWebhookUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      signal: AbortSignal.timeout(15_000),
      body: JSON.stringify(body),
    });
    if (!makeRes.ok) {
      throw new Error(`Make.com responded ${makeRes.status}`);
    }
  } catch (err) {
    console.error('[submit] Make.com webhook failed:', err);
    return new Response(JSON.stringify({ ok: false, error: 'webhook_failed' }), {
      status: 502,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  return new Response(JSON.stringify({ ok: true }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' },
  });
};
